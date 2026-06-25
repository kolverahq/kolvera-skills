#!/usr/bin/env python3
"""Build per-skill release zips for kolvera-skills.

Each skill is a folder containing a SKILL.md. For Claude's "upload a skill"
flow the zip must have the skill FOLDER at its root (e.g. map-the-market/SKILL.md).

Produces, in dist/:
  <skill>.zip         one per skill folder (folder at zip root)
  kolvera-skills-all.zip   bundle of every per-skill zip (unzip, then upload each)

Run:  python build-release-zips.py
"""
import os
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"


def skill_dirs():
    for skill_md in ROOT.rglob("SKILL.md"):
        if "dist" in skill_md.parts:
            continue
        yield skill_md.parent


def zip_folder(folder: Path, out: Path):
    """Zip `folder` so its own name is the top-level entry in the archive."""
    parent = folder.parent
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(folder.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(parent).as_posix())


def main():
    DIST.mkdir(exist_ok=True)
    for f in DIST.glob("*.zip"):
        f.unlink()

    made = []
    for d in sorted(skill_dirs()):
        out = DIST / f"{d.name}.zip"
        zip_folder(d, out)
        made.append(out)
        print(f"  {out.name}  ({out.stat().st_size:,} bytes)  <- {d.relative_to(ROOT).as_posix()}")

    bundle = DIST / "kolvera-skills-all.zip"
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as z:
        for out in made:
            z.write(out, out.name)
    print(f"\n  {bundle.name}  ({bundle.stat().st_size:,} bytes)  <- {len(made)} skill zips")
    print(f"\nDone. {len(made)} skills -> {DIST}")


if __name__ == "__main__":
    main()
