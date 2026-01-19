#!/usr/bin/env python3
"""
Start one or more servers, wait for them to be ready, run a command, then clean up.

Examples:
  python scripts/with_server.py --server "npm run dev" --port 3000 -- python /tmp/ui_check.py
  python scripts/with_server.py \\
    --server "cd backend && python server.py" --port 8000 \\
    --server "cd frontend && npm run dev" --port 3000 \\
    -- python /tmp/ui_check.py
"""

from __future__ import annotations

import argparse
import socket
import subprocess
import sys
import time
from typing import List


def is_server_ready(port: int, timeout: int) -> bool:
    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection(("localhost", port), timeout=1):
                return True
        except OSError:
            time.sleep(0.5)
    return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a command with one or more servers.")
    parser.add_argument("--server", action="append", dest="servers", required=True, help="Server command (repeatable)")
    parser.add_argument("--port", action="append", dest="ports", type=int, required=True, help="Port for each server")
    parser.add_argument("--timeout", type=int, default=45, help="Timeout in seconds per server (default: 45)")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="Command to run after server(s) are ready")
    args = parser.parse_args()

    if args.command and args.command[0] == "--":
        args.command = args.command[1:]
    if not args.command:
        raise SystemExit("No command specified (use -- to separate).")
    if len(args.servers) != len(args.ports):
        raise SystemExit("Number of --server and --port arguments must match.")

    procs: List[subprocess.Popen[str]] = []
    try:
        for idx, (cmd, port) in enumerate(zip(args.servers, args.ports), start=1):
            print(f"Starting server {idx}/{len(args.servers)} on port {port}: {cmd}")
            proc = subprocess.Popen(cmd, shell=True)
            procs.append(proc)
            print(f"Waiting for port {port}...")
            if not is_server_ready(port, args.timeout):
                raise RuntimeError(f"Server failed to start on port {port} within {args.timeout}s")
            print(f"Ready: localhost:{port}")

        print(f"\nAll {len(procs)} server(s) ready.")
        print(f"Running: {' '.join(args.command)}\n")
        result = subprocess.run(args.command)
        raise SystemExit(result.returncode)
    finally:
        print(f"\nStopping {len(procs)} server(s)...")
        for idx, proc in enumerate(procs, start=1):
            try:
                proc.terminate()
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait()
            print(f"Server {idx} stopped")


if __name__ == "__main__":
    main()

