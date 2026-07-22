#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import io
import tempfile
import zipfile
from contextlib import redirect_stderr
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "fetch_skin_pack.py"


def load_module():
    spec = importlib.util.spec_from_file_location("fetch_skin_pack", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_pack(zip_path: Path, prefix: str = "caishen-readable") -> None:
    with zipfile.ZipFile(zip_path, "w") as archive:
        archive.writestr(f"{prefix}/theme.json", "{}")
        archive.writestr(f"{prefix}/background.png", b"fake png bytes")
        archive.writestr(f"{prefix}/README.md", "# Test pack\n")


def test_stage_pack_preserves_existing_until_validated() -> None:
    module = load_module()
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_root = Path(temp_dir)
        zip_path = temp_root / "caishen-readable.zip"
        make_pack(zip_path)

        def fake_download(url: str, destination: Path) -> None:
            destination.write_bytes(zip_path.read_bytes())

        module.download = fake_download
        first = module.stage_pack("caishen-readable", temp_root / "out")
        (first / "keep.txt").write_text("old pack remains until replacement succeeds", encoding="utf-8")

        def failing_download(url: str, destination: Path) -> None:
            raise RuntimeError("network down")

        module.download = failing_download
        try:
            module.stage_pack("caishen-readable", temp_root / "out")
        except RuntimeError:
            pass
        else:
            raise AssertionError("expected failed download")

        assert (first / "keep.txt").exists()


def test_safe_extract_rejects_path_traversal() -> None:
    module = load_module()
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_root = Path(temp_dir)
        bad_zip = temp_root / "bad.zip"
        with zipfile.ZipFile(bad_zip, "w") as archive:
            archive.writestr("../escape.txt", "no")

        with redirect_stderr(io.StringIO()):
            try:
                module.safe_extract(bad_zip, temp_root / "out")
            except SystemExit:
                return
        raise AssertionError("expected unsafe path to fail")


if __name__ == "__main__":
    test_stage_pack_preserves_existing_until_validated()
    test_safe_extract_rejects_path_traversal()
    print("OK: fetch_skin_pack smoke tests passed.")
