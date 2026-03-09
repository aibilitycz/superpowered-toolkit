#!/usr/bin/env node

/**
 * Superpowered Toolkit CLI
 *
 * Install superpowered-toolkit plugins into Cursor, or other AI editors.
 *
 * Usage:
 *   bunx superpowered-toolkit install --to cursor [--output <path>] [--verbose]
 *   npx superpowered-toolkit install --to cursor [--output <path>] [--verbose]
 */

import { existsSync, mkdirSync, readFileSync, writeFileSync, readdirSync, statSync, copyFileSync } from "node:fs";
import { join, resolve, basename, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const PLUGINS_DIR = resolve(__dirname, "..", "plugins");

// ---------------------------------------------------------------------------
// Frontmatter parsing
// ---------------------------------------------------------------------------

function parseFrontmatter(text) {
  if (!text.startsWith("---")) return { meta: {}, body: text };
  const end = text.indexOf("\n---", 3);
  if (end === -1) return { meta: {}, body: text };
  const raw = text.slice(4, end);
  const body = text.slice(end + 4).replace(/^\n+/, "");
  const meta = {};
  for (const line of raw.split("\n")) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;
    const idx = trimmed.indexOf(":");
    if (idx === -1) continue;
    const key = trimmed.slice(0, idx).trim();
    let val = trimmed.slice(idx + 1).trim().replace(/^["']|["']$/g, "");
    if (val.startsWith(">")) val = "";
    if (val.startsWith("[") && val.endsWith("]")) {
      val = val.slice(1, -1).split(",").map(v => v.trim().replace(/^["']|["']$/g, ""));
    }
    meta[key] = val;
  }
  return { meta, body };
}

function formatMdc(frontmatter, body) {
  const lines = ["---"];
  for (const [key, val] of Object.entries(frontmatter)) {
    if (typeof val === "boolean") lines.push(`${key}: ${val}`);
    else if (typeof val === "string") lines.push(`${key}: ${val}`);
    else lines.push(`${key}: ${val}`);
  }
  lines.push("---", "", body);
  return lines.join("\n") + "\n";
}

// ---------------------------------------------------------------------------
// Content transforms
// ---------------------------------------------------------------------------

function normalizeName(name) {
  return (name || "")
    .trim().toLowerCase()
    .replace(/[\\/]+/g, "-")
    .replace(/[:\s]+/g, "-")
    .replace(/[^a-z0-9_-]+/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-+|-+$/g, "") || "item";
}

function transformContent(text) {
  let result = text;

  // 1. Task agent calls → skill invocation
  result = result.replace(
    /^(\s*-?\s*)Task\s+([a-z][a-z0-9_-]*)\(([^)]+)\)/gm,
    (_, prefix, agent, args) => `${prefix}Use the ${normalizeName(agent)} rule to: ${args.trim()}`
  );

  // 2. Slash command namespace flattening
  const skipWords = new Set(["dev", "tmp", "etc", "usr", "var", "bin", "home"]);
  result = result.replace(
    /(?<![:\w])\/([a-z][a-z0-9_:-]*?)(?=[\s,."')}\]`]|$)/gi,
    (match, cmd) => {
      if (skipWords.has(cmd) || cmd.includes("/")) return match;
      if (cmd.includes(":")) cmd = cmd.split(":").pop();
      return `/${cmd}`;
    }
  );

  // 3. Path rewriting
  result = result.replaceAll("~/.claude/", "~/.cursor/");
  result = result.replaceAll(".claude/", ".cursor/");

  // 4. Agent references
  result = result.replace(
    /@([a-z][a-z0-9-]*-(?:agent|reviewer|researcher|analyst|specialist|oracle|sentinel|guardian|strategist))/gi,
    (_, name) => `the ${normalizeName(name)} rule`
  );

  // 5. Knowledge file references → "see the {plugin} rule"
  result = result.replace(
    /(?:\.\.\/)+(?:([a-z-]+)\/)?knowledge\/([a-z-]+)\.md/g,
    (match, plugin, file) => {
      const topic = file.replace(/-/g, " ");
      if (plugin) return `the ${plugin} rule (${topic} section)`;
      return `the composite rule (${topic} section)`;
    }
  );

  return result;
}

// ---------------------------------------------------------------------------
// File system helpers
// ---------------------------------------------------------------------------

function readText(path) {
  return readFileSync(path, "utf-8");
}

function writeText(path, content) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, content, "utf-8");
}

function writeJson(path, data) {
  writeText(path, JSON.stringify(data, null, 2) + "\n");
}

function copyDirRecursive(src, dest) {
  mkdirSync(dest, { recursive: true });
  for (const entry of readdirSync(src)) {
    const srcPath = join(src, entry);
    const destPath = join(dest, entry);
    if (statSync(srcPath).isDirectory()) {
      copyDirRecursive(srcPath, destPath);
    } else {
      copyFileSync(srcPath, destPath);
    }
  }
}

function listFiles(dir, ext) {
  if (!existsSync(dir)) return [];
  return readdirSync(dir)
    .filter(f => f.endsWith(ext) && statSync(join(dir, f)).isFile())
    .sort()
    .map(f => join(dir, f));
}

function listDirs(dir) {
  if (!existsSync(dir)) return [];
  return readdirSync(dir)
    .filter(f => statSync(join(dir, f)).isDirectory() && !f.startsWith("."))
    .sort()
    .map(f => join(dir, f));
}

// ---------------------------------------------------------------------------
// Plugin discovery
// ---------------------------------------------------------------------------

const PSYCHOMETRIC_DOMAINS = [
  "irt", "reliability", "validity", "item-design", "scoring",
  "ai-assessment", "statistics", "io-psychology", "ethics", "references",
];

const GLOB_SCOPED = {
  "python-fastapi-patterns": "**/*.py",
  "typescript-nextjs-patterns": "**/*.{ts,tsx,js,jsx}",
  "infrastructure-ops": "**/*.{tf,yaml,yml,Dockerfile}",
};

function discoverPlugins(pluginsDir) {
  const plugins = [];

  for (const pluginDir of listDirs(pluginsDir)) {
    const pluginJson = join(pluginDir, ".claude-plugin", "plugin.json");
    if (!existsSync(pluginJson)) continue;

    const meta = JSON.parse(readText(pluginJson));
    const name = basename(pluginDir);

    // CLAUDE.md
    let claudeMdBody = "";
    const claudeMdPath = join(pluginDir, "CLAUDE.md");
    if (existsSync(claudeMdPath)) {
      claudeMdBody = parseFrontmatter(readText(claudeMdPath)).body;
    }

    // Skills
    const skills = [];
    for (const skillDir of listDirs(join(pluginDir, "skills"))) {
      const skillMd = join(skillDir, "SKILL.md");
      if (!existsSync(skillMd)) continue;
      const raw = readText(skillMd);
      const { meta: sMeta, body } = parseFrontmatter(raw);
      skills.push({ name: sMeta.name || basename(skillDir), path: skillDir, meta: sMeta, body, raw });
    }

    // Agents
    const agents = [];
    for (const agentFile of listFiles(join(pluginDir, "agents"), ".md")) {
      const raw = readText(agentFile);
      const { meta: aMeta, body } = parseFrontmatter(raw);
      agents.push({ name: aMeta.name || basename(agentFile, ".md"), path: agentFile, meta: aMeta, body });
    }

    // Knowledge
    const knowledge = [];
    for (const kf of listFiles(join(pluginDir, "knowledge"), ".md")) {
      knowledge.push({ name: basename(kf, ".md"), path: kf, content: readText(kf) });
    }

    plugins.push({ name, version: meta.version || "0.0.0", description: meta.description || "", path: pluginDir, claudeMdBody, skills, agents, knowledge });
  }

  return plugins;
}

// ---------------------------------------------------------------------------
// Knowledge resolution
// ---------------------------------------------------------------------------

function buildKnowledgeIndex(plugins) {
  const index = {};
  for (const plugin of plugins) {
    for (const kf of plugin.knowledge) {
      index[kf.name] = kf;
    }
  }
  return index;
}

function resolveKnowledgeRefs(skillBody, knowledgeIndex) {
  const refs = [];
  const seen = new Set();

  // Match: `../../super-integration/knowledge/autonomy-modes.md`
  for (const match of skillBody.matchAll(/`(?:\.\.\/)+[^`\s]+\/knowledge\/([^`\s]+)\.md`/g)) {
    const filename = match[1];
    if (seen.has(filename)) continue;
    seen.add(filename);
    if (knowledgeIndex[filename]) {
      refs.push({ ...knowledgeIndex[filename], relRef: match[0].slice(1, -1) });
    }
  }

  // Match: `../knowledge/decision-frameworks.md` or `knowledge/foo.md`
  for (const match of skillBody.matchAll(/`(?:\.\.\/)?knowledge\/([^`\s]+)\.md`/g)) {
    const filename = match[1];
    if (seen.has(filename)) continue;
    seen.add(filename);
    if (knowledgeIndex[filename]) {
      refs.push({ ...knowledgeIndex[filename], relRef: match[0].slice(1, -1) });
    }
  }

  return refs;
}

function resolvePsychometricDomains(skillPath, skillName, skillBody) {
  const domains = [];
  if (skillName === "psychometric-advisor") {
    for (const domain of PSYCHOMETRIC_DOMAINS) {
      const f = join(skillPath, `${domain}.md`);
      if (existsSync(f)) domains.push({ name: domain, content: readText(f) });
    }
  } else if (skillName === "item-designer" || skillName === "scoring-reviewer") {
    const advisorDir = join(dirname(skillPath), "psychometric-advisor");
    if (existsSync(advisorDir)) {
      for (const match of skillBody.matchAll(/skills\/psychometric-advisor\/([a-z-]+\.md)/g)) {
        const f = join(advisorDir, match[1]);
        if (existsSync(f)) domains.push({ name: basename(f, ".md"), content: readText(f) });
      }
    }
  }
  return domains;
}

// ---------------------------------------------------------------------------
// Converters
// ---------------------------------------------------------------------------

function convertSkill(skill, knowledgeIndex, verbose) {
  const knowledgeRefs = resolveKnowledgeRefs(skill.body, knowledgeIndex);
  const domains = resolvePsychometricDomains(skill.path, skill.name, skill.body);

  let output = skill.raw;

  // Replace knowledge reference lines
  for (const ref of knowledgeRefs) {
    output = output.replaceAll(
      `\`${ref.relRef}\``,
      `\`${ref.name}\` (inlined below)`
    );
  }

  // Append inlined knowledge
  if (knowledgeRefs.length > 0 || domains.length > 0) {
    output += "\n\n---\n\n# Inlined Knowledge\n\n";
    output += "_The following knowledge files have been inlined for Cursor compatibility._\n\n";
  }

  for (const ref of knowledgeRefs) {
    const { body: kb } = parseFrontmatter(ref.content);
    output += `## Inlined: ${ref.name}\n\n${kb.trim()}\n\n`;
  }

  for (const domain of domains) {
    const { body: db } = parseFrontmatter(domain.content);
    output += `## Domain: ${domain.name}\n\n${db.trim()}\n\n`;
  }

  output = transformContent(output);

  // Find extra files (not SKILL.md, not psychometric domains)
  const extraFiles = [];
  if (existsSync(skill.path)) {
    for (const f of readdirSync(skill.path)) {
      if (f === "SKILL.md") continue;
      const full = join(skill.path, f);
      if (statSync(full).isFile() && f.endsWith(".md") && !PSYCHOMETRIC_DOMAINS.includes(basename(f, ".md"))) {
        extraFiles.push(full);
      }
    }
  }

  if (verbose) {
    console.log(`  Skill: ${skill.name} — ${knowledgeRefs.length} knowledge refs, ${domains.length} domains inlined`);
  }

  return { name: skill.name, content: output, extraFiles, knowledgeCount: knowledgeRefs.length + domains.length };
}

function convertAgent(agent, verbose) {
  let description = agent.meta.description || `Converted from agent ${agent.name}`;
  if (Array.isArray(description)) description = description.join(" ");
  description = description.split(/\s+/).join(" ");

  const body = transformContent(agent.body.trim());

  if (verbose) console.log(`  Agent rule: ${agent.name}`);

  return {
    name: normalizeName(agent.name),
    content: formatMdc({ description, alwaysApply: false }, body),
  };
}

function convertPluginComposite(plugin, verbose) {
  const topics = plugin.knowledge.map(k => k.name.replace(/-/g, " ").replace(/\b\w/g, c => c.toUpperCase()));
  const description = topics.length
    ? `${plugin.name} principles and knowledge: ${topics.join(", ")}`
    : `${plugin.name} principles`;

  const parts = [];
  if (plugin.claudeMdBody) parts.push(plugin.claudeMdBody.trim());

  for (const kf of plugin.knowledge) {
    const { body: kb } = parseFrontmatter(kf.content);
    const title = kf.name.replace(/-/g, " ").replace(/\b\w/g, c => c.toUpperCase());
    parts.push(`## ${title}\n\n${kb.trim()}`);
  }

  const body = transformContent(parts.join("\n\n---\n\n"));

  if (verbose) console.log(`  Composite rule: ${plugin.name} (${plugin.knowledge.length} knowledge files)`);

  return { name: plugin.name, content: formatMdc({ description, alwaysApply: false }, body) };
}

function convertGlobRules(plugins, verbose) {
  const rules = [];
  for (const plugin of plugins) {
    for (const kf of plugin.knowledge) {
      if (GLOB_SCOPED[kf.name]) {
        const globs = GLOB_SCOPED[kf.name];
        const { body: kb } = parseFrontmatter(kf.content);
        const title = kf.name.replace(/-/g, " ").replace(/\b\w/g, c => c.toUpperCase());
        const body = transformContent(kb.trim());
        rules.push({ name: kf.name, content: formatMdc({ description: title, globs, alwaysApply: false }, body) });
        if (verbose) console.log(`  Glob rule: ${kf.name} → ${globs}`);
      }
    }
  }
  return rules;
}

function convertRootRule(pluginsDir, verbose) {
  const claudeMd = join(pluginsDir, "..", "CLAUDE.md");
  let body;

  if (existsSync(claudeMd)) {
    const { body: fullBody } = parseFrontmatter(readText(claudeMd));
    const lines = [];
    let inSection = false;
    for (const line of fullBody.split("\n")) {
      if (line.startsWith("## Key Rules") || line.startsWith("## Plugins")) inSection = true;
      else if (line.startsWith("## ") && inSection) inSection = false;
      if (inSection) lines.push(line);
    }
    body = `# Superpowered Toolkit\n\n${lines.length ? lines.join("\n").trim() : fullBody.slice(0, 2000)}`;
  } else {
    body = "# Superpowered Toolkit\n\n5 AI-powered plugins for methodology-grounded development workflows.";
  }

  body = transformContent(body);
  if (verbose) console.log(`  Root rule: superpowered-toolkit (${body.split("\n").length} lines)`);

  return {
    name: "superpowered-toolkit",
    content: formatMdc({ description: "Superpowered Toolkit core principles and plugin overview", alwaysApply: true }, body),
  };
}

// ---------------------------------------------------------------------------
// Validation
// ---------------------------------------------------------------------------

function validate(outputDir) {
  const warnings = [];

  const checkFile = (filePath) => {
    const content = readText(filePath);
    const rel = filePath.replace(outputDir + "/", "");

    // Unresolved knowledge refs (skip inlined notes)
    for (const match of content.matchAll(/\.\.\/\.\.\/[a-z-]+\/knowledge\/[a-z-]+\.md/g)) {
      const lineStart = content.lastIndexOf("\n", match.index) + 1;
      const lineEnd = content.indexOf("\n", match.index + match[0].length);
      const line = content.slice(lineStart, lineEnd === -1 ? undefined : lineEnd);
      if (!line.includes("inlined below") && !line.includes("Inlined:")) {
        warnings.push(`Unresolved knowledge ref in ${rel}: ${match[0]}`);
      }
    }

    // Unconverted .claude/ paths
    if (content.includes(".claude/")) {
      warnings.push(`Unconverted .claude/ path in ${rel}`);
    }
  };

  const walk = (dir) => {
    for (const entry of readdirSync(dir)) {
      const full = join(dir, entry);
      if (statSync(full).isDirectory()) walk(full);
      else if (entry.endsWith(".md") || entry.endsWith(".mdc")) checkFile(full);
    }
  };

  if (existsSync(outputDir)) walk(outputDir);
  return warnings;
}

// ---------------------------------------------------------------------------
// Main: install command
// ---------------------------------------------------------------------------

function install(target, outputPath, verbose) {
  if (target !== "cursor") {
    console.error(`Error: unsupported target "${target}". Available: cursor`);
    process.exit(1);
  }

  const output = resolve(outputPath || ".");

  console.log(`\n  superpowered-toolkit → ${target}\n`);
  console.log(`  Discovering plugins...`);

  const plugins = discoverPlugins(PLUGINS_DIR);
  const totalSkills = plugins.reduce((n, p) => n + p.skills.length, 0);
  const totalAgents = plugins.reduce((n, p) => n + p.agents.length, 0);
  const totalKnowledge = plugins.reduce((n, p) => n + p.knowledge.length, 0);

  console.log(`  Found ${plugins.length} plugins (${totalSkills} skills, ${totalAgents} agents, ${totalKnowledge} knowledge files)\n`);

  const knowledgeIndex = buildKnowledgeIndex(plugins);
  const allRules = [];
  const allSkills = [];
  let totalInlined = 0;

  // Convert skills
  if (verbose) console.log("  Converting skills...");
  for (const plugin of plugins) {
    for (const skill of plugin.skills) {
      const converted = convertSkill(skill, knowledgeIndex, verbose);
      allSkills.push(converted);
      totalInlined += converted.knowledgeCount;
    }
  }

  // Convert agents
  if (verbose) console.log("\n  Converting agents...");
  for (const plugin of plugins) {
    for (const agent of plugin.agents) {
      allRules.push(convertAgent(agent, verbose));
    }
  }

  // Composite plugin rules
  if (verbose) console.log("\n  Generating composite rules...");
  for (const plugin of plugins) {
    allRules.push(convertPluginComposite(plugin, verbose));
  }

  // Glob-scoped rules
  if (verbose) console.log("\n  Generating glob rules...");
  allRules.push(...convertGlobRules(plugins, verbose));

  // Root always-on rule
  if (verbose) console.log("\n  Generating root rule...");
  allRules.push(convertRootRule(PLUGINS_DIR, verbose));

  // Write output
  const rulesDir = join(output, "rules");
  const skillsDir = join(output, "skills");

  for (const rule of allRules) {
    writeText(join(rulesDir, `${rule.name}.mdc`), rule.content);
  }

  for (const skill of allSkills) {
    writeText(join(skillsDir, skill.name, "SKILL.md"), skill.content);
    for (const extra of skill.extraFiles) {
      copyFileSync(extra, join(skillsDir, skill.name, basename(extra)));
    }
  }

  // Manifest
  writeJson(join(output, "manifest.json"), {
    generator: "superpowered-toolkit",
    generatedAt: new Date().toISOString(),
    plugins: Object.fromEntries(plugins.map(p => [p.name, p.version])),
    stats: { rules: allRules.length, skills: allSkills.length, knowledgeFilesInlined: totalInlined },
  });

  // Validate
  const warnings = validate(output);

  // Summary
  const globCount = allRules.filter(r => r.content.includes("globs:") && !r.content.includes('globs: ""')).length;
  console.log(`  ✓ ${allRules.length} rules (${allRules.length - globCount - 1} agent-requested, ${globCount} glob-scoped, 1 always-on)`);
  console.log(`  ✓ ${allSkills.length} skills (${totalInlined} knowledge files inlined)`);

  if (warnings.length > 0) {
    console.log(`\n  ⚠ ${warnings.length} warnings:`);
    for (const w of warnings) console.log(`    ${w}`);
  }

  console.log(`\n  Installed to ${output}\n`);
}

// ---------------------------------------------------------------------------
// CLI
// ---------------------------------------------------------------------------

function printHelp() {
  console.log(`
  superpowered-toolkit — AI-powered plugins for Claude Code, Cursor, and beyond

  Usage:
    superpowered-toolkit install --to <target> [--output <path>] [--verbose]

  Targets:
    cursor    Generate .cursor/rules/ and .cursor/skills/ for Cursor IDE

  Options:
    --to <target>     Target editor (required)
    --output <path>   Output directory (default: .cursor/ in current directory)
    --verbose, -v     Print detailed progress
    --help, -h        Show this help

  Examples:
    bunx superpowered-toolkit install --to cursor
    bunx superpowered-toolkit install --to cursor --output ./my-project/.cursor
    npx superpowered-toolkit install --to cursor
`);
}

const args = process.argv.slice(2);
const command = args[0];

if (!command || command === "--help" || command === "-h") {
  printHelp();
  process.exit(0);
}

if (command !== "install") {
  console.error(`Unknown command: ${command}. Use "install --to cursor".`);
  process.exit(1);
}

// Parse flags
let target = null;
let outputPath = null;
let verbose = false;

for (let i = 1; i < args.length; i++) {
  if (args[i] === "--to" && args[i + 1]) { target = args[++i]; }
  else if (args[i] === "--output" && args[i + 1]) { outputPath = args[++i]; }
  else if (args[i] === "--verbose" || args[i] === "-v") { verbose = true; }
}

if (!target) {
  console.error("Error: --to <target> is required. Available: cursor");
  process.exit(1);
}

// Default output path based on target
if (!outputPath) {
  if (target === "cursor") outputPath = ".cursor";
}

install(target, outputPath, verbose);
