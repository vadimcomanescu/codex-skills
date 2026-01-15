---
name: frontend-design
description: "Create distinctive, production-grade frontend UI with a bold, intentional aesthetic direction, purposeful layouts, meaningful motion, and strong accessibility. Prefer React + Next.js (TypeScript), but support vanilla HTML/CSS/JS when appropriate."
---

# Frontend Design

Build memorable, functional interfaces with a clear point-of-view (no generic templates). Commit to one aesthetic direction, define tokens, ship accessible + responsive UI, and keep changes scoped.

## Preferred Targets (choose the best fit)
1) **Next.js (TypeScript)**: preferred for production app/marketing routes and design system work.
2) **React (TypeScript)**: preferred for SPA/component libraries outside Next.js.
3) **Vanilla HTML/CSS/JS**: great for static demos, prototypes, and standalone embeds.

## Quick Start (do this first)
1) Ask up to 4 questions:
   - What user and job-to-be-done (what should feel “easy” after the change)?
   - Where does it live (component/route) and what stack? Prefer Next.js/React; vanilla is fine for standalone pages or prototypes.
   - In Next.js: assume App Router (`app/`). Any server/client constraints?
   - Any hard constraints (brand tokens, light/dark, motion limits, must-keep UI parts, perf budgets)?
2) Pick an aesthetic direction + **one signature move**. If vague, propose 2–3 options from `references/aesthetic-playbook.md`.
3) Define tokens (type, palette, spacing, radius, shadows, motion). Keep accents to 1–2.
4) Build structure first (semantic markup + layout), then motion, then polish + QA.

## Guardrails (avoid footguns)
- Keep scope tight: redesign only what the user asked for.
- Reuse existing tokens/components if working in an existing repo; do not introduce a new global styling system unless requested.
- Match complexity to the vision: refined minimalism needs restraint; maximalism needs deliberate structure (not random decoration).
- Respect `prefers-reduced-motion` for all animations.
- Avoid “AI slop” defaults. If the repo already uses a generic font, keep it unless the user explicitly wants new typography.
- Default to shipping code that is easy to maintain: small components, clear hierarchy, minimal dependencies.
- Don’t add new packages (animation libs, UI kits, icon sets) unless the user explicitly asks or the repo already uses them.

## Workflow

### 1) Commit to a direction
- Declare: aesthetic direction, palette mood, type pairing, and the signature move.
- Write a 1–2 sentence design thesis that explains the hierarchy and vibe.
- Use `references/anti-patterns.md` to avoid predictable layouts and cliched palettes.

### 2) Plan tokens and layout (before details)
- Define CSS variables (or a theme object) for:
  - Color: background/surface/ink/muted/accent(+optional accent2)
  - Type: display/body/mono, size scale, line-height
  - Shape: radius scale and border rules
  - Depth: shadow and outline rules
  - Motion: durations + easing + reveal stagger step
- Lay out the page/component skeleton and content hierarchy.
- Reference `references/implementation-patterns.md` for patterns and QA.

### 3) Implement (ship code, not moodboards)
- Start with semantic structure and accessible interactions (keyboard + focus states).
- Build macro layout with Grid; micro layout with Flexbox.
- For Next.js/React, keep components small and composable; prefer CSS Modules or the repo’s existing styling approach.
- Use “link for navigation, button for actions” to keep semantics and keyboard behavior correct.
- Apply the signature move sparingly but decisively (one memorable thing, not ten).
- Add motion as orchestration (one strong page-load + a few micro-interactions), not random flourishes.

### 3a) Next.js implementation notes (when applicable)
- **App Router only**: assume `app/` routing (not `pages/`).
- **Server vs Client**: default to Server Components; add `"use client"` only for interactive islands.
- **Data + state**: keep data fetching on the server when possible; keep client state local and purposeful.
- **Performance**: avoid layout shift (stable heights, predictable grids); keep blur/shadows paint-friendly on mobile.
- **Platform primitives**: prefer `next/link` for navigation and `next/image` for real images when available.
- **Fonts**: if changing typography in Next.js, prefer `next/font` to avoid FOIT/FOUT surprises.
- **Styling**: keep it consistent—CSS Modules, Tailwind, or the existing system; don’t introduce a new one without asking.

### 4) Polish and QA
- Responsive pass: collapse grids, maintain padding, preserve CTA prominence on mobile.
- Accessibility pass: landmarks, one `h1`, labels, contrast, focus order, skip link when relevant.
- Performance pass: avoid expensive shadows on mobile, keep animation paint-friendly, avoid large images.

## Definition of Done
- Layout looks intentional at mobile + desktop breakpoints (no cramped type, no orphan CTAs).
- Focus states are visible, tab order is logical, and motion respects `prefers-reduced-motion`.
- Tokens are centralized (CSS variables/theme), and the signature move is present but not overused.

## Deliverables (how to present results)
- List files changed and what they do.
- Explain the aesthetic direction + signature move (1–2 sentences).
- Provide commands to validate (use the repo’s conventions; common ones include `npm run dev`, `npm run lint`, `npm test`).

## Bundled Resources
- `references/aesthetic-playbook.md`: strong directions, type+color cues, signature moves.
- `references/implementation-patterns.md`: layout/motion/a11y patterns for vanilla + React.
- `references/anti-patterns.md`: quick “don’t do this” checklist to avoid generic output.
- `assets/vanilla-starter/`: runnable vanilla starter you can copy + retheme via CSS variables.
- `assets/react-component-starter/`: small React component + CSS module skeleton to retheme.
- `assets/nextjs-app-router-starter/`: minimal Next.js App Router page + tokens you can copy and retheme.
