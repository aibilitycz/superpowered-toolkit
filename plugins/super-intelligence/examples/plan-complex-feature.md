# Example: Planning a Complex Feature

A walkthrough of `/plan` on a complex, multi-repo feature with an existing brainstorm. Demonstrates auto-calibration to DETAILED level, decision rationale, and dependency ordering.

---

## Scenario

A user invokes:

```
/plan docs/brainstorms/2026-02-15-real-time-notifications-brainstorm.md
```

The brainstorm covers adding real-time push notifications across three services: a notification service (new), a WebSocket gateway (existing), and a frontend notification center (new).

## What `/plan` Does

### Step 1: Detect Context

The skill reads the brainstorm and extracts:
- **Decided:** Use Server-Sent Events (SSE) over WebSockets for browser notifications (simpler, sufficient for one-way push)
- **Decided:** Notification preferences stored per-user in the user service (not a separate preferences service)
- **Open question:** Whether to batch notifications or send individually (deferred to implementation)
- **Constraint:** Must work with existing auth tokens, no new auth flow

### Step 2: Research

One subagent scans the codebase:
- Reads the project's CLAUDE.md → finds API conventions, database migration patterns
- Greps for existing notification code → finds email notification service that can be extended
- Checks `docs/solutions/` → surfaces a past solution for SSE connection management with auth tokens

```
>> Known pattern: docs/solutions/infrastructure/sse-auth-token-refresh.md (high match)
```

### Step 3: Calibrate

The skill assesses: Multi-repo (3 services), multi-day (estimated 3-5 days), new service creation, touches auth. **DETAILED plan.**

"This is a detailed plan — multi-repo work with a new service and auth integration. Includes alternatives considered and phased implementation. Let me know if you want to adjust."

### Step 4: Write the Plan

The skill writes `docs/plans/2026-02-15-feat-real-time-notifications-plan.md`:

```markdown
---
title: "feat: Real-time push notifications via SSE"
type: feat
status: active
date: 2026-02-15
brainstorm: docs/brainstorms/2026-02-15-real-time-notifications-brainstorm.md
---

# feat: Real-time Push Notifications

Add real-time push notifications to the platform using Server-Sent Events (SSE).
Users receive instant notifications for assessment completions, team invitations,
and system alerts.

## Problem Statement

Users currently discover events (assessment complete, invitation received) only
by refreshing the page or receiving an email. This creates a 5-15 minute delay
in time-sensitive flows like team onboarding.

## Proposed Solution

SSE-based notification stream from a new notification service, consumed by a
frontend notification center component. User preferences control which
notification types are delivered.

## Decision Rationale

**Why SSE over WebSockets:**
The brainstorm evaluated both. SSE wins because notifications are one-way
(server → client), SSE auto-reconnects on network drops, and our existing
API gateway supports SSE without configuration changes. WebSockets would
require a separate upgrade path and connection management.

**Why preferences in user service (not separate service):**
Notification preferences are a user setting — 3 boolean fields. Creating
a separate service for this adds operational overhead with no benefit.
If preferences grow complex (per-channel, per-type), reconsider.

**Open decision: batching vs. individual:**
Deferred to implementation. Start with individual notifications. If volume
causes performance issues, add batching with a 5-second window.

## Implementation Phases

### Phase 1: Notification Service + Data Model (Day 1-2)
- [ ] Create notification service scaffold (FastAPI, following backend-service pattern)
- [ ] Add notifications table: id, user_id, type, title, body, read, created_at
- [ ] Add user_notification_preferences table: user_id, email_enabled, push_enabled, types_filter
- [ ] Create POST /api/notifications endpoint (internal, for other services to create notifications)
- [ ] Create GET /api/notifications/stream SSE endpoint with auth token validation
- [ ] Write integration tests for notification creation and SSE stream

**Exit criteria:** SSE endpoint streams test notifications to authenticated users.

### Phase 2: Frontend Notification Center (Day 2-3)
- [ ] Create NotificationCenter component with bell icon and unread count
- [ ] Implement SSE connection with auth token and auto-reconnect
- [ ] Add notification dropdown with mark-as-read
- [ ] Apply existing design tokens for notification styling
- [ ] Write component tests for connection lifecycle and display

**Exit criteria:** Frontend shows live notifications from the SSE stream.

### Phase 3: Integration + Producers (Day 3-4)
- [ ] Add notification producer to assessment completion flow
- [ ] Add notification producer to team invitation flow
- [ ] Add user preferences UI in settings page
- [ ] Write end-to-end test: assessment completes → notification appears

**Exit criteria:** Real events trigger real notifications end-to-end.

## Risk Analysis

| Risk | Impact | Mitigation |
|------|--------|------------|
| SSE connections exhaust server resources | High | Connection limit per user (max 3). Heartbeat timeout at 30s. |
| Auth token expires during long SSE connection | Medium | Use past solution: docs/solutions/infrastructure/sse-auth-token-refresh.md |
| Notification volume spikes during batch assessment | Medium | Start with individual delivery. Add batching if needed (deferred decision). |

## Acceptance Criteria

- [ ] Authenticated users receive real-time notifications via SSE
- [ ] Notification preferences control delivery per type
- [ ] Assessment completion and team invitation trigger notifications
- [ ] SSE connection auto-reconnects on network drop
- [ ] Unread count badge updates in real time
```

### Step 5: Offer Next Steps

```
Plan ready at docs/plans/2026-02-15-feat-real-time-notifications-plan.md

Options:
- Review it and refine → I'll adjust based on your feedback
- /document-review → structured evaluation before starting
- /work → start implementing
```

## What This Demonstrates

- **Brainstorm detection:** The plan automatically reads and cross-references brainstorm decisions, skipping redundant questions.
- **Auto-calibration:** Multi-repo + new service + auth = DETAILED plan. No ceremony, no asking the user to pick a level.
- **Decision rationale:** "Why SSE over WebSockets" and "Why preferences in user service" explain the reasoning, not just the choice. Someone reading this plan 6 months later understands WHY.
- **Past solution surfacing:** The SSE auth token refresh solution is surfaced before the user hits that problem.
- **Dependency ordering:** Phases are ordered by dependency — service before frontend, frontend before integration. Each phase has exit criteria.
- **Deferred decisions:** The batching question is explicitly deferred with a trigger for when to revisit it.
