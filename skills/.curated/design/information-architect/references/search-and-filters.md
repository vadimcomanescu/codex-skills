# Search and Filters (IA)

Search does not replace information architecture. Use it to handle scale and ambiguity, while keeping navigation stable and learnable.

## Decide: Navigation vs Search vs Filters
- **Navigation**: “I want *that area* of the product.” (places)
- **Search**: “I know what I’m looking for, but not where it lives.” (lookup)
- **Filters/facets**: “Show me items that match criteria.” (explore)

## When Search Becomes Critical
Search is a primary surface when:
- The collection is large (hundreds/thousands of items).
- Names are memorable identifiers (tickets, customers, docs).
- Users often jump directly to a known item.

In that case, define:
- Where search lives (global vs local)
- What it searches (scope)
- What the results show (grouping and ranking)

## Facets and Filters (keep it simple)
- Prefer 3–6 high-signal facets over 20 low-signal ones.
- Make facets match user intent, not database columns.
- Favor multi-select only when users naturally want “A and B”.
- Provide quick “clear” and visible applied filters (chips).
- Defaults should be safe and explainable (e.g., “Last 30 days”).

## Result Structure (wayfinding for search)
- Group results by type when the system has multiple entity types (Docs vs Projects vs Customers).
- Show enough context to disambiguate:
  - type badge, owner, workspace, last updated, status
- Use empty states that teach:
  - what was searched, why none matched, and what to try next

## Permissions and Personalization
- Don’t leak existence: results must respect permissions.
- If “recent” or “assigned to me” exists, keep the rules transparent and consistent.

## Naming and Governance
If filters/tags are user-generated:
- Define who can create/rename/merge tags.
- Provide a deprecation path to prevent tag sprawl.
- Ensure synonyms map to one canonical term (at least internally).

