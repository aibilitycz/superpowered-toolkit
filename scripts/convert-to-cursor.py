#!/usr/bin/env python3
"""Convert superpowered-toolkit Claude Code plugins to Cursor-compatible format.

Produces:
  - .cursor/skills/     Skills with knowledge inlined (self-contained)
  - .cursor/rules/      Agent rules (.mdc) + composite plugin rules + glob-scoped rules
  - manifest.json       Conversion metadata

Usage:
  python scripts/convert-to-cursor.py [--source plugins/] [--output dist/cursor/] [--verbose] [--dry-run]
"""

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# Frontmatter parsing (stdlib only — no PyYAML dependency)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split YAML frontmatter from markdown body. Returns (meta, body)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 4:].lstrip("\n")
    meta = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val.startswith(">"):
                val = ""  # multiline — skip for now
            if val.startswith("[") and val.endswith("]"):
                val = [v.strip().strip('"').strip("'") for v in val[1:-1].split(",")]
            meta[key] = val
    return meta, body


def format_mdc(frontmatter: dict, body: str) -> str:
    """Format a Cursor .mdc file with YAML frontmatter."""
    lines = ["---"]
    for key, val in frontmatter.items():
        if isinstance(val, bool):
            lines.append(f"{key}: {'true' if val else 'false'}")
        elif isinstance(val, str):
            if "\n" in val or '"' in val:
                lines.append(f'{key}: "{val}"')
            else:
                lines.append(f"{key}: {val}")
        else:
            lines.append(f"{key}: {val}")
    lines.append("---")
    lines.append("")
    lines.append(body)
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Content transforms (matching compound-engineering's proven patterns)
# ---------------------------------------------------------------------------

def transform_content(text: str) -> str:
    """Apply all content transforms for Cursor compatibility."""
    result = text

    # 1. Task agent calls: Task agent-name(args) → Use the agent-name rule to: args
    result = re.sub(
        r"^(\s*-?\s*)Task\s+([a-z][a-z0-9_-]*)\(([^)]+)\)",
        lambda m: f"{m.group(1)}Use the {normalize_name(m.group(2))} rule to: {m.group(3).strip()}",
        result,
        flags=re.MULTILINE,
    )

    # 2. Slash command namespace flattening: /namespace:command → /command
    def flatten_slash(m):
        cmd = m.group(1)
        # Don't flatten filesystem paths
        if cmd in ("dev", "tmp", "etc", "usr", "var", "bin", "home"):
            return m.group(0)
        if "/" in cmd:
            return m.group(0)
        if ":" in cmd:
            cmd = cmd.split(":")[-1]
        return f"/{cmd}"

    result = re.sub(
        r"(?<![:\w])\/([a-z][a-z0-9_:-]*?)(?=[\s,.\"\')}\]`]|$)",
        flatten_slash,
        result,
        flags=re.IGNORECASE,
    )

    # 3. Path rewriting: .claude/ → .cursor/
    result = result.replace("~/.claude/", "~/.cursor/")
    result = result.replace(".claude/", ".cursor/")

    # 4. Agent reference: @agent-name → the agent-name rule
    result = re.sub(
        r"@([a-z][a-z0-9-]*-(?:agent|reviewer|researcher|analyst|specialist|oracle|sentinel|guardian|strategist))",
        lambda m: f"the {normalize_name(m.group(1))} rule",
        result,
        flags=re.IGNORECASE,
    )

    return result


def normalize_name(name: str) -> str:
    """Normalize a name to kebab-case."""
    name = name.strip().lower()
    name = re.sub(r"[\\/]+", "-", name)
    name = re.sub(r"[:\s]+", "-", name)
    name = re.sub(r"[^a-z0-9_-]+", "-", name)
    name = re.sub(r"-+", "-", name)
    return name.strip("-") or "item"


# ---------------------------------------------------------------------------
# Plugin discovery and parsing
# ---------------------------------------------------------------------------

class Plugin:
    def __init__(self, path: Path):
        self.path = path
        self.name = path.name
        self.version = "0.0.0"
        self.description = ""
        self.claude_md_meta: dict = {}
        self.claude_md_body: str = ""
        self.skills: list[dict] = []      # [{name, path, meta, body}]
        self.agents: list[dict] = []      # [{name, path, meta, body}]
        self.knowledge: list[dict] = []   # [{name, path, content}]

    def __repr__(self):
        return f"Plugin({self.name}, v{self.version}, {len(self.skills)}s/{len(self.agents)}a/{len(self.knowledge)}k)"


def discover_plugins(source: Path) -> list[Plugin]:
    """Discover all plugins under the source directory."""
    plugins = []
    for plugin_dir in sorted(source.iterdir()):
        if not plugin_dir.is_dir() or plugin_dir.name.startswith("."):
            continue
        plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
        if not plugin_json.exists():
            continue

        p = Plugin(plugin_dir)

        # Parse plugin.json
        with open(plugin_json) as f:
            meta = json.load(f)
        p.version = meta.get("version", "0.0.0")
        p.description = meta.get("description", "")

        # Parse CLAUDE.md
        claude_md = plugin_dir / "CLAUDE.md"
        if claude_md.exists():
            text = claude_md.read_text()
            p.claude_md_meta, p.claude_md_body = parse_frontmatter(text)

        # Discover skills
        skills_dir = plugin_dir / "skills"
        if skills_dir.exists():
            for skill_dir in sorted(skills_dir.iterdir()):
                if not skill_dir.is_dir():
                    continue
                skill_md = skill_dir / "SKILL.md"
                if not skill_md.exists():
                    continue
                text = skill_md.read_text()
                meta, body = parse_frontmatter(text)
                p.skills.append({
                    "name": meta.get("name", skill_dir.name),
                    "path": skill_dir,
                    "meta": meta,
                    "body": body,
                    "raw": text,
                })

        # Discover agents
        agents_dir = plugin_dir / "agents"
        if agents_dir.exists():
            for agent_file in sorted(agents_dir.glob("*.md")):
                text = agent_file.read_text()
                meta, body = parse_frontmatter(text)
                p.agents.append({
                    "name": meta.get("name", agent_file.stem),
                    "path": agent_file,
                    "meta": meta,
                    "body": body,
                })

        # Discover knowledge files
        knowledge_dir = plugin_dir / "knowledge"
        if knowledge_dir.exists():
            for kf in sorted(knowledge_dir.glob("*.md")):
                p.knowledge.append({
                    "name": kf.stem,
                    "path": kf,
                    "content": kf.read_text(),
                })

        plugins.append(p)

    return plugins


# ---------------------------------------------------------------------------
# Knowledge resolution
# ---------------------------------------------------------------------------

# Map of knowledge file references (relative path patterns) → glob patterns for Cursor
GLOB_SCOPED_KNOWLEDGE = {
    "python-fastapi-patterns": "**/*.py",
    "typescript-nextjs-patterns": "**/*.{ts,tsx,js,jsx}",
    "infrastructure-ops": "**/*.{tf,yaml,yml,Dockerfile}",
}

# Psychometric domain files that live inside the skill directory (not in knowledge/)
PSYCHOMETRIC_DOMAINS = [
    "irt", "reliability", "validity", "item-design", "scoring",
    "ai-assessment", "statistics", "io-psychology", "ethics", "references",
]


def resolve_knowledge_refs(skill_body: str, skill_dir: Path, all_plugins: list[Plugin]) -> list[dict]:
    """Find all knowledge file references in a skill and resolve them.

    Knowledge refs in SKILL.md use relative paths like ../../super-knowledge/knowledge/foo.md
    but these don't resolve correctly from the filesystem because they're designed for
    Claude Code's runtime context. Instead, we extract the filename and search all plugins.
    """
    refs = []
    seen_names = set()

    # Build a lookup of all knowledge files across all plugins
    knowledge_index: dict[str, dict] = {}
    for plugin in all_plugins:
        for kf in plugin.knowledge:
            knowledge_index[kf["name"]] = kf

    # Match all .md file references that look like knowledge paths
    # Patterns: `../../super-integration/knowledge/autonomy-modes.md`
    #           `../knowledge/decision-frameworks.md`
    for match in re.finditer(r"`((?:\.\./)+[^`\s]+/knowledge/([^`\s]+)\.md)`", skill_body):
        rel_path = match.group(1)
        filename = match.group(2)
        if filename in seen_names:
            continue
        seen_names.add(filename)
        if filename in knowledge_index:
            kf = knowledge_index[filename]
            refs.append({
                "name": filename,
                "path": kf["path"],
                "content": kf["content"],
                "rel_ref": rel_path,
            })

    # Also match simple refs like: `../knowledge/decision-frameworks.md`
    # or: `knowledge/socratic-patterns.md` (without ../../ prefix)
    for match in re.finditer(r"`(?:\.\./)?knowledge/([^`\s]+)\.md`", skill_body):
        filename = match.group(1)
        if filename in seen_names:
            continue
        seen_names.add(filename)
        if filename in knowledge_index:
            kf = knowledge_index[filename]
            refs.append({
                "name": filename,
                "path": kf["path"],
                "content": kf["content"],
                "rel_ref": f"knowledge/{filename}.md",
            })

    return refs


def resolve_psychometric_domains(skill_dir: Path) -> list[dict]:
    """Resolve psychometric domain files for skills that reference them."""
    # Domain files live directly in the skill directory (e.g., skills/psychometric-advisor/irt.md)
    domains = []
    for domain_name in PSYCHOMETRIC_DOMAINS:
        domain_file = skill_dir / f"{domain_name}.md"
        if domain_file.exists():
            domains.append({
                "name": domain_name,
                "path": domain_file,
                "content": domain_file.read_text(),
            })
    return domains


# ---------------------------------------------------------------------------
# Skill conversion (Strategy 1: inline knowledge)
# ---------------------------------------------------------------------------

def convert_skill(skill: dict, all_plugins: list[Plugin], verbose: bool = False) -> dict:
    """Convert a skill with inlined knowledge."""
    skill_path = skill["path"]
    skill_name = skill["name"]
    raw = skill["raw"]

    # Resolve knowledge references (base = skill directory, where SKILL.md lives)
    knowledge_refs = resolve_knowledge_refs(skill["body"], skill_path, all_plugins)

    # Check for psychometric domain files (for psychometric-advisor, item-designer, scoring-reviewer)
    psychometric_domains = []
    if skill_name in ("psychometric-advisor", "item-designer", "scoring-reviewer"):
        if skill_name == "psychometric-advisor":
            # Inline all domains — they're in the same directory as SKILL.md
            psychometric_domains = resolve_psychometric_domains(skill_path)
        else:
            # For item-designer and scoring-reviewer, find referenced domain files
            # References look like: `skills/psychometric-advisor/scoring.md` (relative to plugin root)
            advisor_dir = skill_path.parent / "psychometric-advisor"
            if advisor_dir.exists():
                for match in re.finditer(r"skills/psychometric-advisor/([a-z-]+\.md)", skill["body"]):
                    domain_file = advisor_dir / match.group(1)
                    if domain_file.exists():
                        psychometric_domains.append({
                            "name": domain_file.stem,
                            "path": domain_file,
                            "content": domain_file.read_text(),
                        })

    # Start with original content
    output = raw

    # Replace knowledge reference lines with inline notes
    for ref in knowledge_refs:
        # Replace "See `path`" lines
        output = output.replace(
            f"See `{ref['rel_ref']}`",
            f'(See "Inlined: {ref["name"]}" section below)',
        )
        # Replace backtick references in other contexts
        output = output.replace(
            f"`{ref['rel_ref']}`",
            f'`{ref["name"]}` (inlined below)',
        )

    # Append inlined knowledge
    if knowledge_refs or psychometric_domains:
        output += "\n\n---\n\n# Inlined Knowledge\n\n"
        output += "_The following knowledge files have been inlined for Cursor compatibility._\n\n"

    for ref in knowledge_refs:
        _, kb = parse_frontmatter(ref["content"])
        output += f"## Inlined: {ref['name']}\n\n{kb.strip()}\n\n"

    for domain in psychometric_domains:
        _, db = parse_frontmatter(domain["content"])
        output += f"## Domain: {domain['name']}\n\n{db.strip()}\n\n"

    # Apply content transforms
    output = transform_content(output)

    # Collect extra files from skill directory (scripts/, references/, etc.)
    extra_files = []
    for item in skill_path.iterdir():
        if item.name == "SKILL.md":
            continue
        if item.is_file() and item.suffix == ".md":
            # Don't include psychometric domain files — they're inlined
            if item.stem in PSYCHOMETRIC_DOMAINS:
                continue
            extra_files.append(item)

    if verbose:
        print(f"  Skill: {skill_name} — {len(knowledge_refs)} knowledge refs, {len(psychometric_domains)} domains inlined")

    return {
        "name": skill_name,
        "content": output,
        "extra_files": extra_files,
        "knowledge_count": len(knowledge_refs) + len(psychometric_domains),
    }


# ---------------------------------------------------------------------------
# Agent conversion (→ .mdc rules)
# ---------------------------------------------------------------------------

def convert_agent(agent: dict, verbose: bool = False) -> dict:
    """Convert an agent to a Cursor .mdc rule."""
    description = agent["meta"].get("description", f"Converted from agent {agent['name']}")
    if isinstance(description, list):
        description = " ".join(description)
    # Clean multiline descriptions
    description = " ".join(description.split())

    body = transform_content(agent["body"].strip())

    frontmatter = {
        "description": description,
        "alwaysApply": False,
    }

    if verbose:
        print(f"  Agent rule: {agent['name']}")

    return {
        "name": normalize_name(agent["name"]),
        "content": format_mdc(frontmatter, body),
    }


# ---------------------------------------------------------------------------
# Composite plugin rules (Strategy 3: merge CLAUDE.md + knowledge)
# ---------------------------------------------------------------------------

def convert_plugin_composite(plugin: Plugin, verbose: bool = False) -> dict:
    """Create a composite .mdc rule from plugin CLAUDE.md + knowledge files."""
    topics = [k["name"].replace("-", " ").title() for k in plugin.knowledge]
    description = f"{plugin.name} principles and knowledge: {', '.join(topics)}" if topics else f"{plugin.name} principles"

    # Build body: CLAUDE.md first, then knowledge files
    parts = []
    if plugin.claude_md_body:
        parts.append(plugin.claude_md_body.strip())

    for kf in plugin.knowledge:
        _, kb = parse_frontmatter(kf["content"])
        title = kf["name"].replace("-", " ").title()
        parts.append(f"## {title}\n\n{kb.strip()}")

    body = transform_content("\n\n---\n\n".join(parts))

    frontmatter = {
        "description": description,
        "alwaysApply": False,
    }

    if verbose:
        print(f"  Composite rule: {plugin.name} ({len(plugin.knowledge)} knowledge files)")

    return {
        "name": plugin.name,
        "content": format_mdc(frontmatter, body),
    }


# ---------------------------------------------------------------------------
# Glob-scoped language rules
# ---------------------------------------------------------------------------

def convert_glob_rules(plugins: list[Plugin], verbose: bool = False) -> list[dict]:
    """Create glob-scoped .mdc rules for language-specific knowledge."""
    rules = []
    for plugin in plugins:
        for kf in plugin.knowledge:
            if kf["name"] in GLOB_SCOPED_KNOWLEDGE:
                globs = GLOB_SCOPED_KNOWLEDGE[kf["name"]]
                _, kb = parse_frontmatter(kf["content"])
                title = kf["name"].replace("-", " ").title()

                frontmatter = {
                    "description": title,
                    "globs": globs,
                    "alwaysApply": False,
                }

                body = transform_content(kb.strip())
                rules.append({
                    "name": kf["name"],
                    "content": format_mdc(frontmatter, body),
                })

                if verbose:
                    print(f"  Glob rule: {kf['name']} → {globs}")

    return rules


# ---------------------------------------------------------------------------
# Root always-on rule
# ---------------------------------------------------------------------------

def convert_root_rule(source: Path, verbose: bool = False) -> dict:
    """Create the root always-on .mdc rule from the toolkit's CLAUDE.md."""
    claude_md = source.parent / "CLAUDE.md"
    if not claude_md.exists():
        # Fallback: generate minimal rule
        body = "# Superpowered Toolkit\n\n5 AI-powered plugins for methodology-grounded development workflows."
    else:
        text = claude_md.read_text()
        _, full_body = parse_frontmatter(text)

        # Extract just the Key Rules and Plugins sections — keep it minimal
        lines = []
        in_section = False
        for line in full_body.splitlines():
            if line.startswith("## Key Rules") or line.startswith("## Plugins"):
                in_section = True
            elif line.startswith("## ") and in_section:
                in_section = False
            if in_section:
                lines.append(line)

        body = "\n".join(lines).strip() if lines else full_body[:2000]
        body = f"# Superpowered Toolkit\n\n{body}"

    body = transform_content(body)

    frontmatter = {
        "description": "Superpowered Toolkit core principles and plugin overview",
        "alwaysApply": True,
    }

    if verbose:
        print(f"  Root rule: superpowered-toolkit ({len(body.splitlines())} lines)")

    return {
        "name": "superpowered-toolkit",
        "content": format_mdc(frontmatter, body),
    }


# ---------------------------------------------------------------------------
# Output writer
# ---------------------------------------------------------------------------

def write_output(output_dir: Path, rules: list[dict], skills: list[dict], manifest: dict, dry_run: bool = False):
    """Write all converted content to the output directory."""
    rules_dir = output_dir / "rules"
    skills_dir = output_dir / "skills"

    if dry_run:
        print("\n[DRY RUN] Would generate:")
        print(f"  Rules ({len(rules)}):")
        for r in rules:
            lines = r["content"].count("\n")
            print(f"    {rules_dir / (r['name'] + '.mdc')} ({lines} lines)")
        print(f"  Skills ({len(skills)}):")
        for s in skills:
            lines = s["content"].count("\n")
            print(f"    {skills_dir / s['name'] / 'SKILL.md'} ({lines} lines)")
        return

    # Clean output dir
    if output_dir.exists():
        shutil.rmtree(output_dir)

    rules_dir.mkdir(parents=True, exist_ok=True)
    skills_dir.mkdir(parents=True, exist_ok=True)

    # Write rules
    for rule in rules:
        (rules_dir / f"{rule['name']}.mdc").write_text(rule["content"])

    # Write skills
    for skill in skills:
        skill_dir = skills_dir / skill["name"]
        skill_dir.mkdir(parents=True, exist_ok=True)
        (skill_dir / "SKILL.md").write_text(skill["content"])
        # Copy extra files (scripts, references, etc.)
        for extra in skill.get("extra_files", []):
            shutil.copy2(extra, skill_dir / extra.name)

    # Write manifest
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n"
    )


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_output(output_dir: Path) -> list[str]:
    """Validate the converted output. Returns list of warnings."""
    warnings = []

    for f in output_dir.rglob("*.md"):
        content = f.read_text()
        # Check for unresolved knowledge references (skip lines that say "inlined below")
        for match in re.finditer(r"\.\./\.\./[a-z-]+/knowledge/[a-z-]+\.md", content):
            line_start = content.rfind("\n", 0, match.start()) + 1
            line_end = content.find("\n", match.end())
            line = content[line_start:line_end if line_end != -1 else len(content)]
            if "inlined below" in line or "Inlined:" in line:
                continue
            warnings.append(f"Unresolved knowledge ref in {f.relative_to(output_dir)}: {match.group()}")
        # Check for .claude/ paths
        for match in re.finditer(r"\.claude/", content):
            warnings.append(f"Unconverted .claude/ path in {f.relative_to(output_dir)}")
            break  # One warning per file

    for f in output_dir.rglob("*.mdc"):
        content = f.read_text()
        if not content.startswith("---"):
            warnings.append(f"Missing frontmatter in {f.relative_to(output_dir)}")
        for match in re.finditer(r"\.claude/", content):
            warnings.append(f"Unconverted .claude/ path in {f.relative_to(output_dir)}")
            break

    return warnings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Convert superpowered-toolkit to Cursor format")
    parser.add_argument("--source", type=Path, default=Path("plugins"),
                        help="Source plugins directory (default: plugins/)")
    parser.add_argument("--output", type=Path, default=Path("dist/cursor"),
                        help="Output directory (default: dist/cursor/)")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Print detailed progress")
    parser.add_argument("--dry-run", "-n", action="store_true",
                        help="Print what would be generated without writing")
    args = parser.parse_args()

    source = args.source.resolve()
    output = args.output.resolve()

    if not source.exists():
        print(f"Error: source directory not found: {source}", file=sys.stderr)
        sys.exit(1)

    # Phase 1: Discover plugins
    print(f"Discovering plugins in {source}...")
    plugins = discover_plugins(source)
    print(f"Found {len(plugins)} plugins: {', '.join(p.name for p in plugins)}")

    total_skills = sum(len(p.skills) for p in plugins)
    total_agents = sum(len(p.agents) for p in plugins)
    total_knowledge = sum(len(p.knowledge) for p in plugins)
    print(f"  {total_skills} skills, {total_agents} agents, {total_knowledge} knowledge files")

    # Phase 2 + 3: Convert everything
    all_rules: list[dict] = []
    all_skills: list[dict] = []
    total_inlined = 0

    print("\nConverting skills (with knowledge inlining)...")
    for plugin in plugins:
        for skill in plugin.skills:
            converted = convert_skill(skill, plugins, verbose=args.verbose)
            all_skills.append(converted)
            total_inlined += converted["knowledge_count"]

    print(f"\nConverting agents to .mdc rules...")
    for plugin in plugins:
        for agent in plugin.agents:
            all_rules.append(convert_agent(agent, verbose=args.verbose))

    print(f"\nGenerating composite plugin rules...")
    for plugin in plugins:
        all_rules.append(convert_plugin_composite(plugin, verbose=args.verbose))

    print(f"\nGenerating glob-scoped language rules...")
    all_rules.extend(convert_glob_rules(plugins, verbose=args.verbose))

    print(f"\nGenerating root always-on rule...")
    all_rules.append(convert_root_rule(source, verbose=args.verbose))

    # Phase 4: Write output
    manifest = {
        "generator": "superpowered-toolkit/scripts/convert-to-cursor.py",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": str(source),
        "plugins": {p.name: p.version for p in plugins},
        "stats": {
            "rules": len(all_rules),
            "skills": len(all_skills),
            "knowledge_files_inlined": total_inlined,
        },
    }

    print(f"\nWriting output to {output}...")
    write_output(output, all_rules, all_skills, manifest, dry_run=args.dry_run)

    # Validation
    if not args.dry_run:
        print(f"\nValidating output...")
        warnings = validate_output(output)
        if warnings:
            print(f"  {len(warnings)} warnings:")
            for w in warnings:
                print(f"    ⚠ {w}")
        else:
            print(f"  No warnings.")

    # Summary
    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Conversion complete:")
    print(f"  {len(all_rules)} rules ({sum(1 for r in all_rules if 'alwaysApply' not in r['content'] or 'true' not in r['content'])} agent-requested, "
          f"{sum(1 for r in all_rules if 'globs:' in r['content'] and 'globs: \"\"' not in r['content'])} glob-scoped, "
          f"1 always-on)")
    print(f"  {len(all_skills)} skills ({total_inlined} knowledge files inlined)")
    if not args.dry_run:
        print(f"  Output: {output}")


if __name__ == "__main__":
    main()
