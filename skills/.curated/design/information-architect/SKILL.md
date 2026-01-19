---
name: information-architect
description: "World-class information architecture workflows for product and design teams: define navigation, taxonomy, labeling, content models, and page hierarchy so complex products feel obvious. Use when designing or redesigning an app/website structure, menus, docs/knowledge base IA, onboarding flows, search/filtering, permissions-based navigation, or when turning a messy feature set into a coherent system."
---

# Information Architect

Make complex products feel simple by giving users a consistent mental model: clear hierarchy, stable navigation, predictable labels, and strong wayfinding.

This skill is for designing the *structure* (what goes where and why). Pair with `frontend-design` when you also need a UI/visual redesign.

## Quick Start (do this first)
1) Ask up to 5 questions:
  - Who are the primary users and their top 3 jobs-to-be-done (and what must feel “easy”)?
  - What surface is this (web app, marketing site, docs/KB, mobile app)? Any SEO, i18n, or accessibility constraints?
  - What exists today (current nav/sitemap), what’s broken, and what must not change?
  - What are the “things” in the system (entities/content types) and what are the “actions” users do to/with them?
  - Any hard constraints: permissions/roles, compliance, product strategy, roadmap, or analytics targets?
2) Choose one primary organizing principle (one “north star”):
  - task-first, object-first, lifecycle-based, audience-based, or frequency-based (see `references/ia-models-and-principles.md`)
3) Produce the minimum set of IA artifacts (in this order):
  - **IA thesis** (1–2 sentences): the organizing logic + how users will find things
  - **Map**: sitemap/app map (`SITEMAP.mmd`; template in `assets/ia-docs/`)
  - **Navigation spec**: global + local + contextual nav rules (`NAVIGATION.md`; template in `assets/ia-docs/`)
  - **Labeling & naming rules**: consistent labels, verbs/nouns, capitalization (`references/labeling-and-microcopy.md`)
  - **Taxonomy/metadata** (only if needed): tags/facets + ownership rules (`TAXONOMY.csv`; template in `assets/ia-docs/`)

## Guardrails (utmost simplicity)
- Prefer fewer, clearer choices over “complete” categorization. Users scan; they don’t read.
- Keep top-level navigation small and stable. If everything is top-level, nothing is.
- Don’t mix organizing principles at the same level (e.g., “By Team” next to “Settings” next to “Reports”).
- Avoid duplicate pathways unless the user benefit is explicit (and labeled consistently).
- Use progressive disclosure: reveal complexity when it becomes relevant; keep early steps lightweight.
- Names are UX: labels must match user language, not org structure or internal terminology.
- Optimize for *wayfinding*: users should always know where they are, what’s here, and what’s next.
- When in doubt, scan `references/anti-patterns.md` and delete complexity.

## Workflow

### 1) Frame the problem with evidence
- Inventory the current structure:
  - Pages/routes, features, docs sections, settings, admin areas, and entry points
  - User roles/permissions and their access differences
- Collect signals:
  - Top tasks, search logs, support tickets, analytics funnels, “where did you expect to find this?”
- Output:
  - A scoped inventory (`CONTENT_INVENTORY.csv`; template: `assets/ia-docs/CONTENT_INVENTORY.csv`)
  - A short problem statement: what is hard to find/understand today and for whom

### 2) Define the mental model (what the product *is*)
- Decide what your system is “about” in user terms:
  - What are the primary entities (things) and primary actions (verbs)?
  - What are the stable categories vs dynamic filters/tags?
- Write the IA thesis (1–2 sentences):
  - Example: “Organize by customer lifecycle; use role-based entry points; keep tools contextual to the object.”
- Output:
  - Draft entity list + relationships (`CONTENT_MODEL.md`; template: `assets/ia-docs/CONTENT_MODEL.md`)

### 3) Design the structure (map → navigation → page types)
- Start with the map:
  - Sitemap/app map that shows hierarchy, not pixels (`SITEMAP.mmd`; template: `assets/ia-docs/SITEMAP.mmd`)
- Then define navigation layers:
  - Global nav: 5–7 items max unless there’s strong evidence otherwise
  - Local nav: within a section (tabs/side nav) based on section tasks
  - Contextual nav: within an object/workflow (e.g., “Actions”, “Related”, “History”)
- Define page types and hierarchy:
  - Landing/overview pages should answer “what can I do here?”
  - Detail pages should be object-first (what it is) then actions (what I can do)
- Output:
  - Navigation rules + “what belongs where” (`NAVIGATION.md`; template: `assets/ia-docs/NAVIGATION.md`)

### 4) Create the classification system (only as complex as needed)
- Choose the lightest taxonomy that supports the jobs:
  - Categories for stable groupings, facets for filtering, tags for loose labeling
- Define ownership and governance:
  - Who can create tags? Who merges/renames? What’s the deprecation process?
- Ensure search and IA agree:
  - If search is critical, design facets and result grouping intentionally (see `references/search-and-filters.md`)
- Output:
  - Taxonomy + facet definitions (`TAXONOMY.csv`; template: `assets/ia-docs/TAXONOMY.csv`)

### 5) Validate quickly (before polishing)
- Run “findability” checks:
  - Tree-test critical tasks (“Where would you click to…?”)
  - Card sort when categories are unclear or political
- Look for: wrong first clicks, label confusion, deep nesting, and duplicate categories.
- Output:
  - A short change log: what changed and why (`DECISIONS.md`; template: `assets/ia-docs/DECISIONS.md`)
- When to read more: load `references/research-and-validation.md` for scripts and facilitation tips.

### 6) Handoff for design + engineering (make it shippable)
- Provide implementation notes:
  - Route/URL conventions, nav component requirements, permission rules, redirects/deprecations
  - Analytics: name key events by task and surface
- Coordinate with UI:
  - Pair with `frontend-design` to ensure visual hierarchy supports the IA hierarchy (no competing CTAs, clear headings, consistent surfaces).
- Output:
  - A single IA package under `docs/ia` with the artifacts above (use the scaffold tool below)

## Optional tool: scaffold an IA documentation pack
```bash
python ~/.codex/skills/information-architect/scripts/scaffold_ia_docs.py . --out docs/ia --force
```

## Definition of Done
- Users can correctly predict where the top tasks live (and are right most of the time).
- Global navigation is stable, small, and uses user language (not org charts).
- Each section has a clear purpose, clear entry points, and no “misc dumping ground”.
- Taxonomy (if present) has ownership rules and avoids tag sprawl.
- The IA maps cleanly to routes/pages/components and can be implemented without guesswork.

## Deliverables (how to present results)
- Start with the IA thesis + the organizing principle.
- Provide the sitemap/app map and navigation rules.
- Call out key trade-offs and open questions.
- List files/docs produced (prefer `docs/ia/*`).

## Bundled Resources
- Models + principles: `references/ia-models-and-principles.md`
- Labeling + microcopy rules: `references/labeling-and-microcopy.md`
- Search + filters guidance: `references/search-and-filters.md`
- Research methods (tree testing, card sort): `references/research-and-validation.md`
- Anti-patterns (what to avoid): `references/anti-patterns.md`
- Restructures and migrations: `references/migration-and-governance.md`
- Doc templates: `assets/ia-docs/`
