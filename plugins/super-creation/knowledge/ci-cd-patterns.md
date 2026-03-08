# CI/CD Patterns

Read this when working on GitHub Actions workflows, Dockerfiles, deployment pipelines, or release processes. Covers build optimization, deployment strategies, and rollback procedures.

## Why This Matters

CI/CD pipelines are infrastructure-as-code that runs on every commit. A slow pipeline wastes developer time across every PR. An unreliable pipeline erodes trust — teams start skipping CI or merging without green checks. A secure pipeline is the last line of defense before code reaches production.

## GitHub Actions Workflow Patterns

**Caching — the biggest speed win:**
```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip  # or node_modules, .gradle, etc.
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements*.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

Cache by lockfile hash. If the lockfile hasn't changed, skip the install entirely. Common cache targets:
- Python: `~/.cache/pip` or `~/.cache/uv`
- Node: `node_modules` (or `~/.npm` for npm cache)
- Go: `~/go/pkg/mod`
- Docker layers: `type=gha` with BuildKit

**Matrix builds** for testing across versions:
```yaml
strategy:
  matrix:
    python-version: ['3.11', '3.12']
    node-version: ['20', '22']
  fail-fast: false  # Don't cancel other jobs if one fails
```

**Reusable workflows** (DRY for CI):
```yaml
# .github/workflows/reusable-test.yml
on:
  workflow_call:
    inputs:
      service:
        required: true
        type: string
```
Call from other workflows with `uses: ./.github/workflows/reusable-test.yml`.

**Secrets handling:**
- Never echo secrets — `echo ${{ secrets.KEY }}` leaks to logs
- Use `environment` protection rules for production deploys
- Prefer OIDC (`id-token: write`) over long-lived service account keys [strong]
- Pin action versions to SHA, not tags: `uses: actions/checkout@abc123` not `@v4`

**Common workflow mistakes:**
- Missing `concurrency` — multiple runs of the same workflow on the same branch race each other
- `pull_request` vs `pull_request_target` — `pull_request_target` runs with write access, dangerous for fork PRs
- Fat runners — running full test suites when only docs changed. Use path filters.

## Docker Multi-Stage Build Patterns

**The pattern:** Separate build dependencies from runtime:
```dockerfile
# Build stage — has compilers, dev deps
FROM python:3.12 AS builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt
COPY . .

# Runtime stage — minimal image
FROM python:3.12-slim
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app
USER 1000
CMD ["python", "-m", "app"]
```

**Layer caching optimization:**
- Copy dependency files FIRST, install deps, THEN copy source code
- Source changes rebuild only the last `COPY` — deps are cached
- Order from least-changed to most-changed

**Security hardening:**
- `USER 1000` (numeric, not named) — Kubernetes needs numeric for `runAsNonRoot`
- No secrets in build args or layers — use `--mount=type=secret`
- `.dockerignore` everything that isn't needed: `.git`, tests, docs, `.env`
- Scan images: `trivy image <name>` or `grype <name>`

**Size optimization:**
- Use `-slim` or `-alpine` base images
- Remove package manager caches: `rm -rf /var/lib/apt/lists/*`
- Combine related `RUN` commands to reduce layers
- Multi-stage: only copy the built artifact to the final stage

## Deployment Pipeline Structure

**Standard pipeline stages:**

```
Build → Test → Scan → Deploy (dev) → Verify → Deploy (prod) → Verify
```

| Stage | Purpose | Gate |
|-------|---------|------|
| **Build** | Compile, bundle, create artifacts | Builds successfully |
| **Test** | Unit tests, integration tests | All pass, coverage meets threshold |
| **Scan** | Security scan, license check | No critical/high vulnerabilities |
| **Deploy (dev)** | Deploy to development environment | Deployment succeeds, health checks pass |
| **Verify (dev)** | Smoke tests, synthetic checks | Key user flows work |
| **Deploy (prod)** | Deploy to production | Manual approval (for high-risk changes) |
| **Verify (prod)** | Production smoke tests, metrics check | Error rate stable, latency stable |

**Deploy verification checklist:**
- Health endpoint returns 200
- Key API endpoints respond correctly
- Error rate hasn't increased (compare to pre-deploy baseline)
- Latency hasn't degraded
- No new error patterns in logs

## Rollback Procedures

**Automated rollback triggers:**
- Error rate exceeds 5% for 5+ minutes after deploy
- Health check failures for 3+ consecutive checks
- p99 latency doubles compared to pre-deploy baseline

**Manual rollback decision tree:**
```
Is the issue affecting users?
├─ Yes → Roll back immediately, investigate after
└─ No → Can it be fixed forward in < 30 minutes?
   ├─ Yes → Fix forward
   └─ No → Roll back, fix in next deploy
```

**Rollback methods (fastest to slowest):**
1. **Kubernetes rollback:** `kubectl rollout undo deployment/<name>` — seconds
2. **Helm rollback:** `helm rollback <release> <revision>` — seconds
3. **Revert commit + redeploy:** `git revert` → push → pipeline runs — minutes
4. **Feature flag disable:** Turn off the flag, code stays deployed — seconds (if flags are set up)

**After rollback:**
- Confirm metrics return to normal
- Write a brief incident note (what happened, what was rolled back, who did it)
- Fix the issue on a branch before redeploying

## Deployment Strategies

| Strategy | Risk | Downtime | Complexity | Use When |
|----------|------|----------|------------|----------|
| **Rolling update** | Low | Zero | Low | Most deployments (K8s default) |
| **Blue-green** | Low | Zero | Medium | Database migrations, full stack changes |
| **Canary** | Lowest | Zero | High | High-traffic services, risky changes |
| **Recreate** | High | Yes | Low | Stateful services that can't run two versions |

## Anti-patterns

- **No caching in CI.** Every run downloads the internet. Cache dependencies aggressively.
- **Testing in production only.** "Works on my machine" and "works in prod" are not testing strategies.
- **Manual deploys.** If deploy requires SSH and running commands, it's not reproducible. Automate it.
- **No rollback plan.** Every deploy should have a documented rollback. "Revert the commit" is a plan. Nothing is not.
- **Secret rotation fear.** If rotating a secret requires a 3-day ceremony, it won't happen. Make rotation easy and frequent.
- **Monolith CI.** Running all tests for all services on every commit. Use path-based triggers to test only what changed.
