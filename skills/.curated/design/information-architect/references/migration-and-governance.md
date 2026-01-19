# Restructures, Migrations, and Governance

Information architecture changes are product changes. Plan for migration, not just a prettier tree.

## When You’re Changing an Existing IA
Default goals:
- Preserve user muscle memory where it matters (critical paths).
- Reduce confusion during transition (clear mapping, redirects, and comms).
- Measure impact (findability, task completion, support tickets).

## Migration Plan Checklist
- **Old → new mapping** for every major destination:
  - what moved, what merged, what was removed, what replaced it
- **Redirect strategy** (web):
  - permanent redirects for moved pages, avoid chains
  - ensure search engines and bookmarks survive (if SEO matters)
- **In-product guidance**:
  - “Where did X go?” helper, release notes, banners for a limited time
- **Permissions review**:
  - ensure the new structure still respects access rules
- **Analytics continuity**:
  - map old events to new events so dashboards don’t go dark

## Governance (prevent drift)
If you introduce categories/tags/facets:
- Define owners for taxonomy changes (merge/rename/deprecate).
- Define allowed creation:
  - open (anyone), moderated, or admin-only
- Define a cleanup policy:
  - stale tags merge into canonical terms; deprecate unused categories

## Deleting or Hiding Content
Don’t create a “graveyard”.

- If something is deprecated, explain what replaces it.
- If you hide by permission, keep the logic transparent (“Contact admin to request access”).
- Maintain consistent URL/route patterns even when features are gated.

