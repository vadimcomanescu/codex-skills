# IA Models and Principles

Use this to pick a clean organizing logic, keep hierarchy coherent, and avoid “misc” sprawl.

## Organizing Principles (pick one primary)

### 1) Task-first (job-based)
**Best when:** users come to *do* a small set of repeatable jobs (create, review, approve, reconcile).

- Global nav labels are verbs or task nouns (“Review”, “Invoices”, “Run payroll”).
- Pages are organized around workflows, not data models.
- Objects still exist, but show up as *inputs/outputs* inside tasks.

**Watch out:** task-first can fragment object information across many places; ensure there’s still a coherent object detail view when needed.

### 2) Object-first (thing-based)
**Best when:** users think in “things” (projects, customers, tickets, campaigns) and actions are contextual.

- Global nav labels are object nouns (“Customers”, “Projects”, “Tickets”).
- Actions live inside the object surfaces (“Create”, “Export”, “Configure”, “History”).

**Watch out:** object-first can hide “cross-object” work (e.g., “Approvals”). If approvals are central, carve out a task-first hub.

### 3) Lifecycle-based (stage-based)
**Best when:** the product is about moving work through stages (intake → draft → review → publish).

- Primary navigation reflects stable stages.
- Each stage has its own overview, queues, and outcomes.

**Watch out:** stage labels must match user language; internal process names don’t transfer.

### 4) Audience-based (role-based)
**Best when:** different audiences use different parts of the product with minimal overlap.

- Entry point is role selection, workspace switching, or dedicated dashboards.
- Navigation is permission-aware and tailored.

**Watch out:** avoid “role silos” if users collaborate across roles; provide shared objects and shared terminology.

### 5) Frequency-based (the 80/20)
**Best when:** a few destinations dominate usage and should be one click away.

- Global nav gives prominence to top tasks/objects.
- Rare tasks move into “Settings”, “Admin”, or contextual locations.

**Watch out:** “frequent” varies by role; validate by role-based analytics, not averages.

## Navigation Layers (design intentionally)

### Global navigation
Use for the stable “major places” in the product.

- Default: 5–7 top-level items unless the domain clearly demands more.
- Each item should have a crisp purpose statement (one sentence).
- Avoid mixing principles at the same level (don’t combine “Reports” + “By Team” + “Settings”).

### Local navigation (within a section)
Use for secondary destinations that share one context.

- Side nav works for many peers (10–20) and when titles are longer.
- Tabs work for a handful of peers (3–7) and when scanning is important.
- Breadcrumbs help when hierarchy matters; tabs help when hierarchy is shallow.

### Contextual navigation (inside an object/workflow)
Use for actions and related views that only make sense *once you’re in context*.

- Group actions by intent (manage, analyze, share, automate) rather than by implementation.
- Prefer one primary action per surface; demote the rest.

## Hierarchy Heuristics (practical)
- Depth: if users regularly go 3+ levels deep, check whether a hub/overview page is missing.
- Breadth: if a menu has 12+ peers, group by a higher-level concept or move rare items to “More”.
- Consistency: labels should stay stable across surfaces; don’t call the same thing “Projects” in one place and “Workspaces” in another.
- Predictability beats cleverness: the goal is “I guessed where it was and I was right.”

## Page Roles (what pages should *do*)
- **Hub/overview**: answer “what is here?” and “what can I do next?”
- **List/collection**: support scanning, filtering, sorting, and bulk actions.
- **Detail/object**: show the object’s identity first; actions second; history/metadata last.
- **Settings/admin**: group by scope (user vs workspace vs org) and risk (safe vs dangerous).

## Wayfinding (make the structure legible)
- Clear page titles that match the nav label.
- Active nav states that match the hierarchy.
- Breadcrumbs when hierarchy is meaningful; otherwise rely on consistent local nav.
- Avoid “dead ends”: always provide a next step (related, create, return to list).

## Docs / Knowledge Base IA (when the surface is documentation)
Docs have different failure modes than apps: users arrive via search, deep links, and shared URLs more often than via global navigation.

Defaults:
- Separate **doc types** in IA:
  - Get started (guided path)
  - Guides/how-to (task-first)
  - Concepts (mental models, “how it works”)
  - Reference (API/CLI/config, exhaustive)
- Keep the **left nav** stable and shallow; use in-page TOCs for depth.
- Design for **versioning** (current vs legacy) and **deprecation** (clear notices + redirects).
- Treat **search** as a first-class surface; invest in facets only if the corpus is large and heterogeneous.

## Marketing / SEO IA (when the surface is a site)
Defaults:
- Use clear, human-readable URL slugs that reflect the hierarchy.
- Avoid orphan pages; every page should have at least one intentional pathway.
- Use breadcrumbs when the hierarchy is meaningful (helps wayfinding and SEO).

## Mobile Navigation Notes
- Global nav usually maps to a tab bar (5 max) or tab bar + “More”.
- Deep hierarchies should lean on search, recent, and scoped collections rather than nested menus.

## “IA Thesis” Template (copy/paste)
Fill in this sentence before designing:

1) “Users primarily think in terms of **[objects or tasks]**.”
2) “We organize the product by **[organizing principle]** so users can **[top job]** quickly.”
3) “We keep **[complexity]** contextual and preserve a stable global nav for **[major places]**.”
