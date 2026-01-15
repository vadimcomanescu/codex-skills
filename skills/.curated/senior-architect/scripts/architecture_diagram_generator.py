#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List

from dependency_analyzer import analyze as analyze_deps  # type: ignore


def _diagram_from_signals(signals: List[str], title: str) -> str:
    has_next = "nextjs" in signals
    has_node_api = "node" in signals or "graphql" in signals
    has_db = "postgres" in signals
    has_cache = "redis" in signals

    lines: List[str] = []
    lines.append("flowchart LR")
    lines.append(f"  %% {title}")
    lines.append("  User[User]")
    lines.append("  Browser[Browser]")
    lines.append("  User --> Browser")

    if has_next:
        lines.append("  Web[Next.js Web]")
        lines.append("  Browser --> Web")
    else:
        lines.append("  Web[Web App]")
        lines.append("  Browser --> Web")

    if has_node_api:
        lines.append("  API[API]")
        lines.append("  Web -->|HTTP| API")

    if has_db:
        lines.append("  DB[(Postgres)]")
        if has_node_api:
            lines.append("  API -->|SQL| DB")
        else:
            lines.append("  Web -->|SQL| DB")

    if has_cache:
        lines.append("  Cache[(Redis)]")
        if has_node_api:
            lines.append("  API --> Cache")
        else:
            lines.append("  Web --> Cache")

    lines.append("")
    lines.append("  %% Add third-party integrations here")
    lines.append("  ThirdParty[3rd-party Service]")
    if has_node_api:
        lines.append("  API --> ThirdParty")
    else:
        lines.append("  Web --> ThirdParty")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a starter Mermaid context/container diagram.")
    parser.add_argument("target", nargs="?", default=".", help="Target directory (default: .)")
    parser.add_argument("--out", required=True, help="Output file path (e.g., docs/architecture/diagram.mmd)")
    parser.add_argument("--title", default="Architecture", help="Diagram title comment")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = (Path.cwd() / out_path).resolve()

    out_path.parent.mkdir(parents=True, exist_ok=True)

    deps = analyze_deps(target)
    signals = deps.get("stack_signals", [])
    if not isinstance(signals, list):
        signals = []

    diagram = _diagram_from_signals([str(s) for s in signals], args.title)
    out_path.write_text(diagram, encoding="utf-8")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()

