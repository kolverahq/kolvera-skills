#!/usr/bin/env python3
"""Check or explicitly refresh each standalone skill's shared references."""
import argparse
from pathlib import Path
import sys

from validate_release import ROOT, ValidationError, skill_dirs


def sync(root: Path, write: bool = False) -> list[str]:
    canonical = root / "contracts/operations.md"
    try:
        data = canonical.read_bytes()
    except OSError as exc:
        raise ValidationError(f"{canonical}: cannot read canonical operations reference: {exc}") from exc
    float_canonical = root / "contracts/float.md"
    float_data = float_canonical.read_bytes() if float_canonical.exists() else None
    differences = []
    for folder in skill_dirs(root):
        references = {"operations.md": data}
        if float_data is not None and folder.name in {"campaign-build", "rmp-campaign"}:
            references["float.md"] = float_data
        for name, reference_data in references.items():
            target = folder / "references" / name
            if target.is_symlink() or target.parent.is_symlink():
                raise ValidationError(f"{target}: symlink not allowed")
            if not target.is_file() or target.read_bytes() != reference_data:
                differences.append(str(target))
                if write:
                    target.parent.mkdir(exist_ok=True)
                    target.write_bytes(reference_data)
    return differences


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="check references without changing files (default)")
    mode.add_argument("--write", action="store_true", help="explicitly refresh references from canonical bytes")
    args = parser.parse_args()
    try:
        changed = sync(args.root.resolve(), args.write)
    except (OSError, ValidationError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if changed and not args.write:
        print("Shared references differ; run scripts/sync_references.py --write:\n" + "\n".join(changed), file=sys.stderr)
        return 1
    print(f"{'Updated' if args.write else 'Checked'} shared references; {len(changed)} differences.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())