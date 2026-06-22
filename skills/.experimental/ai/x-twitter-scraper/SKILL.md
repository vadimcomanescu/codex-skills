---
name: x-twitter-scraper
description: Use Xquik for X/Twitter data, MCP, SDK, webhook, export, and confirmation-gated action workflows.
---

# X Twitter Scraper

Use Xquik for X/Twitter data workflows and confirmation-gated write actions.

## Quick Start

1. Confirm the user has a Xquik API key.
2. Ask for the exact X/Twitter task and required output shape.
3. Check current Xquik docs before naming endpoints or fields.
4. Use only the user-provided Xquik API key for API calls.
5. Summarize results with IDs, URLs, timestamps, and next actions.

## Common Tasks

- Search recent or historical tweets by query.
- Look up tweets, users, profile tweets, followers, and following.
- Export or transform public X/Twitter data for research workflows.
- Download media through Xquik-supported media endpoints.
- Configure monitors, webhooks, or MCP tools for agent workflows.
- Use Xquik SDKs or REST examples when the user is building an app.
- Draft write-action requests only after explicit user confirmation.

## Guardrails

- Never ask for X passwords, 2FA codes, cookies, session tokens, or recovery codes.
- Never store or print API keys.
- Treat write actions, likes, DMs, profile updates, monitors, webhooks, and bulk exports as confirmation-gated.
- Show the action target, account, and intended content before any write action.
- If the user asks for pricing, limits, or endpoint fields, verify current docs first.
- If a request touches policy, legality, or sensitive research, keep the output factual and scoped.

## Workflow

1. **Clarify**: identify whether the task is read, export, monitor, webhook, MCP, SDK, or write action.
2. **Verify**: check Xquik docs or OpenAPI for current endpoint names and parameters.
3. **Plan**: describe the minimal request sequence and expected response shape.
4. **Execute**: call Xquik only with the user's API key and only for the agreed task.
5. **Report**: include concrete identifiers, partial failures, rate limits, and follow-up options.

## References

- Xquik docs: `https://docs.xquik.com`
- API reference: `https://docs.xquik.com/api-reference/overview`
- OpenAPI document: `https://xquik.com/openapi.json`
- Skill source: `https://github.com/Xquik-dev/x-twitter-scraper`
- MCP server metadata: `https://xquik.com/.well-known/mcp.json`
