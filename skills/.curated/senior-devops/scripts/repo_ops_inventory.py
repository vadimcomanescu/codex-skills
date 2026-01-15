#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Tuple


def exists_any(root: Path, rels: List[str]) -> List[str]:
    return [r for r in rels if (root / r).exists()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Inventory repo operational signals (CI/CD, deploy, observability).")
    parser.add_argument("target", nargs="?", default=".", help="Repo root (default: .)")
    parser.add_argument("--out", default="/tmp/ops_inventory.md", help="Output markdown path")
    args = parser.parse_args()

    root = Path(args.target).resolve()
    if not root.exists():
        raise SystemExit(f"Target does not exist: {root}")

    checks: List[Tuple[str, List[str]]] = [
        ("CI workflows", [".github/workflows"]),
        ("Docker", ["Dockerfile", "docker-compose.yml", "docker-compose.yaml"]),
        ("Kubernetes", ["k8s", "kubernetes", "helm", "charts"]),
        ("Terraform/IaC", ["terraform", "infra", "infrastructure", "pulumi.yaml", "Pulumi.yaml"]),
        ("Monitoring config", ["grafana", "prometheus", "datadog", "newrelic", ".sentryclirc"]),
        ("Runbooks", ["runbooks", "docs/runbooks", "docs/ops", "ops"]),
    ]

    found_lines: List[str] = []
    missing_lines: List[str] = []
    for label, paths in checks:
        found = exists_any(root, paths)
        if found:
            found_lines.append(f"- **{label}**: " + ", ".join([f"`{p}`" for p in found]))
        else:
            missing_lines.append(f"- **{label}**: (not found; consider adding)")

    md = "\n".join(
        [
            "# Ops Inventory",
            "",
            f"Target: `{root}`",
            "",
            "## Found",
            *(found_lines or ["- (none)"]),
            "",
            "## Missing / follow-ups",
            *(missing_lines or ["- (none)"]),
            "",
            "## Notes",
            "- This is a heuristic inventory, not a security or reliability guarantee.",
            "- Use it to drive a concrete action list (CI hardening, runbooks, alerts, rollback).",
            "",
        ]
    )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()

