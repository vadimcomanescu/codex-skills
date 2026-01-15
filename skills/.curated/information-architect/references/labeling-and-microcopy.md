# Labeling and Microcopy (IA)

Treat labels as UX infrastructure: users build a map in their head based on repeated words.

## Labeling Rules (default)
- Use the user’s language, not internal org structure or code names.
- Prefer short, concrete labels (1–3 words). Avoid sentences in navigation.
- Choose one grammar pattern per level:
  - **Object-first**: nouns (“Customers”, “Projects”, “Invoices”)
  - **Task-first**: verbs or task nouns (“Review”, “Approve”, “Import”, “Reconciliation”)
- Use consistent casing (recommend sentence case for UI labels unless the product already uses Title Case).
- Avoid near-synonyms across nav (“Billing” vs “Payments” vs “Invoices”). Pick one and standardize.

## Navigation Label Checklist
For each label, answer:
1) Would a user search for this word?
2) Does it describe a *place* (nav) vs an *action* (button)?
3) Is it unique in the UI vocabulary (no duplicates, no near-duplicates)?
4) Does it still make sense out of context (sidebar, breadcrumbs, page title)?

## “Place vs Action” (semantics)
- Navigation = “places” (nouns / destinations).
- Buttons = “actions” (verbs).

If you find verbs in global navigation, double-check that you’re not encoding a workflow that belongs on an overview page.

## Microcopy Principles (simple UX)
- Prefer clarity over personality. The goal is to reduce hesitation.
- Put the key noun early (“Customer name”, not “Name of customer”).
- Use consistent terms for the same concept across UI, docs, and analytics.
- Avoid hidden requirements. If a field is required or irreversible, say so before the user commits.

## Internationalization (i18n) and Accessibility
- Keep labels short to reduce truncation and translation issues.
- Avoid idioms, puns, or culture-specific metaphors.
- Don’t rely on icons alone. If using an icon, pair it with a visible label or an accessible name.

## Pattern: Define a Glossary (small but powerful)
Create a tiny vocabulary list:
- Primary entities (“Customer”, “Project”, “Invoice”)
- Primary actions (“Create”, “Invite”, “Export”)
- Scopes (“Workspace”, “Organization”, “Account”)

Then enforce it in:
- Navigation
- Page titles
- Button labels
- Empty states
- Analytics event names

## Common Labeling Anti-patterns
- **Overloading**: one label means two different things in different places.
- **Inconsistent scope**: “Settings” sometimes means user settings and sometimes org settings.
- **Internal taxonomy leakage**: labels mirror team/org structure (“Ops”, “BizDev”, “Platform”).

