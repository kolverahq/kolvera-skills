#!/usr/bin/env python3
"""Build deterministic, self-contained skill ZIPs and an offline verification manifest.

Run: python build-release-zips.py [--root SOURCE] [--output DIRECTORY]
Only immediate skills/* folders are packaged. Hidden files, caches and compiled
Python payloads are excluded. No live Kolvera tools or credentials are used.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
from validate_release import ValidationError, digest, payload_files, validate_archives, validate_source


def write_zip(out: Path, members: dict[str, bytes]) -> None:
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(members.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data, compresslevel=9)


def build(root: Path, output: Path, expected_count: int | None = None) -> list[Path]:
    if output.is_symlink():
        raise ValidationError("output directory must not be a symlink")
    root, output = root.resolve(), output.resolve()
    if output == root or output.is_relative_to(root / "skills") or output.is_relative_to(root / "contracts"):
        raise ValidationError("output must not overwrite source root, skill folders or contracts")
    contract, folders = validate_source(root, expected_count)
    artifact_names = {f"{folder.name}.zip" for folder in folders} | {"kolvera-skills-all.zip"}
    if output.exists():
        stale = {p.name for p in output.glob("*.zip")} - artifact_names
        if stale:
            raise ValidationError(f"{output}: unexpected existing ZIPs {sorted(stale)}; use a clean output directory")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="kolvera-skills-build-", dir=output.parent) as temporary:
        staging = Path(temporary)
        for folder in folders:
            members = {f"{folder.name}/{path.relative_to(folder).as_posix()}": path.read_bytes() for path in payload_files(folder)}
            write_zip(staging / f"{folder.name}.zip", members)
        write_zip(staging / "kolvera-skills-all.zip", {f"{folder.name}.zip": (staging / f"{folder.name}.zip").read_bytes() for folder in folders})
        manifest = {
            "schema_version": 1,
            "verified_at": contract["verified_at"],
            "product_source_sha": contract["product_source_sha"],
            "skills": [folder.name for folder in folders],
            "artifacts": {name: {"sha256": digest((staging / name).read_bytes()), "size": (staging / name).stat().st_size} for name in sorted(artifact_names)},
        }
        manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")
        (staging / "manifest.json").write_bytes(manifest_bytes)
        checksums = "".join(f"{manifest['artifacts'][name]['sha256']}  {name}\n" for name in sorted(artifact_names))
        checksums += f"{digest(manifest_bytes)}  manifest.json\n"
        (staging / "CHECKSUMS.sha256").write_bytes(checksums.encode("utf-8"))
        validate_archives(root, staging, contract, folders)
        output.mkdir(exist_ok=True)
        # Only named build artifacts are replaced, never unrelated files.
        for source in sorted(staging.iterdir()):
            source.replace(output / source.name)
    return [output / name for name in sorted(artifact_names)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, help="artifact directory (default: SOURCE/dist)")
    parser.add_argument("--expected-count", type=int, help="optional release-specific skill count pin")
    args = parser.parse_args()
    try:
        artifacts = build(args.root, args.output or args.root / "dist", args.expected_count)
    except (OSError, ValidationError) as exc:
        print(f"Build failed:\n{exc}", file=sys.stderr)
        return 1
    print(f"Built {len(artifacts) - 1} skill ZIPs, bundle, manifest and checksums in {artifacts[0].parent}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())