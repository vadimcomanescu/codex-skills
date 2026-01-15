---
name: webapp-testing
description: Local webapp testing workflow using Python + Playwright: start servers, explore DOM, take screenshots, capture console logs, and verify user flows. Use when debugging UI behavior, validating frontend changes, or creating lightweight end-to-end checks for a local dev server.
---

# Web App Testing (Playwright)

Prefer small, targeted Playwright scripts over heavyweight test suites when you need fast UI verification.

## Quick Start
1) Decide what you’re testing:
   - static HTML file (`file://…`) vs local dev server (`http://localhost:…`)
2) Recon first:
   - take a screenshot
   - list buttons/links/inputs
   - capture console logs
3) Then automate:
   - select stable locators
   - assert visible text and URL changes
   - keep timeouts explicit and minimal

## Helper: run a command with dev server(s)
Start one or more servers, wait for ports, run your Playwright script, then clean up:
```bash
python ~/.codex/skills/webapp-testing/scripts/with_server.py --server "npm run dev" --port 3000 -- python /tmp/ui_check.py
```

## Assets
- Playwright examples you can copy: `assets/playwright-examples/`

