#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    import tomllib  # py3.11+
except Exception:  # pragma: no cover
    tomllib = None  # type: ignore


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _safe_json_load(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(_read_text(path))
    except Exception:
        return {}


def _parse_requirements(text: str) -> List[str]:
    deps: List[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-r") or line.startswith("--"):
            continue
        deps.append(re.split(r"[<=>;\\[]", line, maxsplit=1)[0].strip())
    return sorted({d for d in deps if d})


def _parse_go_mod(text: str) -> List[str]:
    in_require_block = False
    deps: List[str] = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("require ("):
            in_require_block = True
            continue
        if in_require_block and s == ")":
            in_require_block = False
            continue
        if s.startswith("require "):
            parts = s.split()
            if len(parts) >= 2:
                deps.append(parts[1])
        elif in_require_block:
            parts = s.split()
            if len(parts) >= 1:
                deps.append(parts[0])
    return sorted({d for d in deps if d and not d.startswith("//")})


def _parse_cargo_toml(text: str) -> List[str]:
    if tomllib is None:
        return []
    try:
        data = tomllib.loads(text)
    except Exception:
        return []
    deps = data.get("dependencies", {})
    if isinstance(deps, dict):
        return sorted(deps.keys())
    return []


def _parse_pyproject(text: str) -> List[str]:
    if tomllib is None:
        return []
    try:
        data = tomllib.loads(text)
    except Exception:
        return []

    deps: List[str] = []

    project = data.get("project", {})
    if isinstance(project, dict):
        project_deps = project.get("dependencies", [])
        if isinstance(project_deps, list):
            deps.extend([re.split(r"[<=>;\\[]", d, maxsplit=1)[0].strip() for d in project_deps])

    tool = data.get("tool", {})
    if isinstance(tool, dict):
        poetry = tool.get("poetry", {})
        if isinstance(poetry, dict):
            poetry_deps = poetry.get("dependencies", {})
            if isinstance(poetry_deps, dict):
                deps.extend([k for k in poetry_deps.keys() if k.lower() != "python"])

    return sorted({d for d in deps if d})


def _detect_stack(dep_index: Dict[str, List[str]]) -> List[str]:
    all_deps = {d.lower() for deps in dep_index.values() for d in deps}
    signals: List[Tuple[str, Iterable[str]]] = [
        ("nextjs", ["next"]),
        ("react", ["react"]),
        ("node", ["express", "fastify", "koa", "hono"]),
        ("graphql", ["graphql", "apollo-server", "@apollo/server", "urql", "@urql/core"]),
        ("postgres", ["pg", "postgres", "postgresql", "psycopg", "psycopg2", "asyncpg"]),
        ("prisma", ["prisma", "@prisma/client"]),
        ("redis", ["redis", "ioredis"]),
        ("python", ["django", "fastapi", "flask"]),
    ]
    detected: List[str] = []
    for name, keys in signals:
        if any(k.lower() in all_deps for k in keys):
            detected.append(name)
    return detected


def analyze(target: Path) -> Dict[str, Any]:
    manifests: Dict[str, Path] = {}
    for name in ["package.json", "pyproject.toml", "go.mod", "Cargo.toml"]:
        p = target / name
        if p.exists():
            manifests[name] = p

    requirements = sorted(target.glob("requirements*.txt"))
    if requirements:
        manifests["requirements.txt"] = requirements[0]

    dep_index: Dict[str, List[str]] = {}

    if "package.json" in manifests:
        pkg = _safe_json_load(manifests["package.json"])
        deps: List[str] = []
        for key in ["dependencies", "devDependencies", "peerDependencies"]:
            section = pkg.get(key, {})
            if isinstance(section, dict):
                deps.extend(section.keys())
        dep_index["npm"] = sorted({d for d in deps if d})

    if "requirements.txt" in manifests:
        dep_index["pip"] = _parse_requirements(_read_text(manifests["requirements.txt"]))

    if "pyproject.toml" in manifests:
        dep_index["pyproject"] = _parse_pyproject(_read_text(manifests["pyproject.toml"]))

    if "go.mod" in manifests:
        dep_index["gomod"] = _parse_go_mod(_read_text(manifests["go.mod"]))

    if "Cargo.toml" in manifests:
        dep_index["cargo"] = _parse_cargo_toml(_read_text(manifests["Cargo.toml"]))

    stack = _detect_stack(dep_index)

    return {
        "target": str(target),
        "manifests": {k: str(v) for k, v in manifests.items()},
        "dependencies": dep_index,
        "stack_signals": stack,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize repo dependencies and stack signals.")
    parser.add_argument("target", nargs="?", default=".", help="Target directory (default: .)")
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    parser.add_argument("--output", help="Write JSON output to a file")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    if not target.exists():
        raise SystemExit(f"Target does not exist: {target}")

    result = analyze(target)

    if args.json or args.output:
        payload = json.dumps(result, indent=2, sort_keys=True)
        if args.output:
            Path(args.output).write_text(payload, encoding="utf-8")
        else:
            print(payload)
        return

    print(f"Target: {result['target']}")
    if result["manifests"]:
        print("Manifests:")
        for k, v in result["manifests"].items():
            print(f"  - {k}: {v}")
    if result["stack_signals"]:
        print("Stack signals:", ", ".join(result["stack_signals"]))
    for mgr, deps in result["dependencies"].items():
        print(f"{mgr}: {len(deps)} deps")


if __name__ == "__main__":
    main()

