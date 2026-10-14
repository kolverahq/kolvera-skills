#!/usr/bin/env python3
"""Offline checks against a dated compatibility snapshot, never live MCP validation."""
from __future__ import annotations

import argparse
import ast
from datetime import date
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {"__pycache__", "node_modules", "cache"}
TOOL_PREFIXES = frozenset(
    "get list create update delete bulk batch find run trigger expand generate search "
    "activate approve dismiss action enrol assign link unlink move diagnose analyze "
    "verify set build ingest add stop review revise preview send withdraw".split()
)
UNSAFE_RULES = (
    (r"if a batch stalls.{0,30}retry in batches", "unsafe stalled-batch replay recipe"),
    (r"(?:run|start|use).{0,15}(?:a )?fresh chat", "unsafe fresh-chat retry workaround"),
    (r"(?:only one job runs|one job per (?:chat|session))", "retired chat-scoped enrichment deduplication"),
    (r"resume (?:it |the campaign )?first", "unsafe resume-before-enrol advice"),
    (r"paused.{0,40}rejects enrol", "incorrect paused-enrolment restriction"),
)


class ValidationError(ValueError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def skill_dirs(root: Path) -> list[Path]:
    directory = root / "skills"
    if not directory.is_dir():
        raise ValidationError(f"{directory}: missing skills directory")
    result = []
    for path in sorted(directory.iterdir()):
        if path.name.startswith("."):
            continue
        if path.is_symlink():
            raise ValidationError(f"{path}: symlink not allowed")
        if path.is_dir():
            result.append(path)
    return result


def payload_files(folder: Path) -> list[Path]:
    """Only visible files in an immediate skills/* folder are release payload."""
    result = []
    for path in sorted(folder.rglob("*")):
        parts = path.relative_to(folder).parts
        if any(p.startswith(".") or p in IGNORED_DIRS for p in parts):
            continue
        if path.is_symlink():
            raise ValidationError(f"{path}: symlink not allowed")
        if path.is_file() and path.suffix.lower() not in {".pyc", ".pyo"}:
            result.append(path)
    return result


def load_contract(root: Path) -> dict:
    path = root / "contracts/kolvera.json"
    try:
        contract = json.loads(path.read_text(encoding="utf-8-sig"))
        date.fromisoformat(contract["verified_at"])
        if not re.fullmatch(r"[0-9a-f]{40}", contract["product_source_sha"]):
            raise ValueError("product_source_sha must be a full lowercase SHA")
        if not isinstance(contract["tools"], dict) or not contract["tools"]:
            raise ValueError("tools must be a nonempty object")
        for name, params in contract["tools"].items():
            if not re.fullmatch(r"[a-z][a-z0-9_]*", name):
                raise ValueError(f"invalid tool name: {name}")
            for kind in ("required", "optional"):
                if not isinstance(params[kind], list) or not all(isinstance(p, str) for p in params[kind]):
                    raise ValueError(f"{name}.{kind} must be a string list")
        if not isinstance(contract["prices"], dict) or not contract["prices"]:
            raise ValueError("prices must be a nonempty object")
        return contract
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise ValidationError(f"{path}: invalid compatibility snapshot: {exc}") from exc


def frontmatter(text: str, label: str) -> dict[str, str]:
    """Read the deliberately small scalar frontmatter schema without a YAML dependency."""
    lines = text.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise ValidationError(f"{label}: missing YAML frontmatter")
    result = {}
    key = None
    for line in lines[1:lines[1:].index("---") + 1]:
        match = re.fullmatch(r"( *)([a-z_][a-z0-9_-]*):\s*(.*)", line)
        if match:
            indent, key, value = match.groups()
            if indent and key not in {"last_verified", "compatible_tools"}:
                continue
            if key in result:
                raise ValidationError(f"{label}: duplicate frontmatter key {key}")
            result[key] = value.strip().strip("\"'")
        elif line.strip() and not line.lstrip().startswith("#"):
            if key and result.get(key) in {">", "|", ">-", "|-"}:
                result[key] = line.strip()
            elif key == "description" and line.startswith(" "):
                result[key] += " " + line.strip()
            else:
                raise ValidationError(f"{label}: unsupported frontmatter syntax: {line}")
    return result


def check_document(text: str, path: Path, folder: Path, tools: dict) -> list[str]:
    errors = []
    label = path.as_posix()
    normalised = re.sub(r"[*_`]+", "", text).lower()
    for pattern, message in UNSAFE_RULES:
        if re.search(pattern, normalised, re.DOTALL):
            errors.append(f"{label}: {message}")
    references = re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)
    references += re.findall(r"`((?:\.?\.?/)?[\w./-]+\.(?:md|json|txt|csv|yaml|yml))`", text)
    if "GUIDELINES.md" in text:
        references.append("GUIDELINES.md")
    for reference in sorted(set(references)):
        reference = reference.strip().split(" ", 1)[0].strip("<>").split("#", 1)[0]
        if not reference or re.match(r"[a-z][a-z0-9+.-]*:", reference, re.I):
            continue
        target = (path.parent / reference).resolve()
        if not target.is_relative_to(folder.resolve()) or not target.is_file():
            errors.append(f"{label}: missing or non-standalone reference {reference}")
        elif target not in payload_files(folder):
            errors.append(f"{label}: reference omitted from archive {reference}")
    for name in sorted(set(re.findall(r"\bmcp__kolvera__([a-z][a-z0-9_]*)\b", text))):
        if name not in tools:
            errors.append(f"{label}: unsupported declared tool mcp__kolvera__{name}")
    # Exact standalone inline-code names with a conventional verb prefix are tool
    # candidates. Schema parameter names are data, even when they start with a
    # verb (send_start_hour, stop_on_reply). Ordinary prose and unprefixed enums
    # remain outside this conservative scan; this is not live API validation.
    field_names = {parameter for schema in tools.values()
                   for kind in ("required", "optional") for parameter in schema[kind]}

    def tool_like(name: str) -> bool:
        prefix, separator, remainder = name.partition("_")
        return bool(separator and remainder and prefix in TOOL_PREFIXES)

    tokens = set(re.findall(r"(?<!`)`([a-z][a-z0-9_]+)`(?!`)", text))
    for name in sorted(tokens - set(tools) - field_names):
        if tool_like(name):
            errors.append(f"{label}: unsupported logical tool token {name}")
    # A call has stronger intent than an inline data token. Unknown tool-like
    # calls fail even if their spelling happens to collide with a schema field.
    for match in re.finditer(r"\b([a-z][a-z0-9_]+)\(([^()\n]*)\)", text):
        name, args = match.groups()
        name = name.removeprefix("mcp__kolvera__")
        if name not in tools:
            if tool_like(name):
                errors.append(f"{label}: unsupported logical tool call {name}")
            continue
        try:
            call = ast.parse(f"{name}({args})", mode="eval").body
        except SyntaxError:
            continue  # Explanatory pseudocode is outside keyword-validation scope.
        allowed = set(tools[name]["required"] + tools[name]["optional"])
        for keyword in call.keywords:
            if keyword.arg is not None and keyword.arg not in allowed:
                errors.append(f"{label}: {name}: unsupported parameter {keyword.arg}")
        if not call.args and all(keyword.arg is not None for keyword in call.keywords):
            provided = {keyword.arg for keyword in call.keywords}
            missing = set(tools[name]["required"]) - provided
            if missing:
                errors.append(f"{label}: {name}: missing required parameters {sorted(missing)}")
        if name == "expand_deep_research" and call.args:
            errors.append(f"{label}: expand_deep_research example must name report_id explicitly")
    return errors


def validate_source(root: Path, expected_count: int | None = None) -> tuple[dict, list[Path]]:
    root = root.resolve()
    contract = load_contract(root)
    folders = skill_dirs(root)
    errors = []
    if not folders:
        errors.append(f"{root}/skills: no skill folders found")
    if expected_count is not None and len(folders) != expected_count:
        errors.append(f"{root}/skills: expected {expected_count} skill folders, found {len(folders)}")
    canonical = root / "contracts/operations.md"
    try:
        canonical_bytes = canonical.read_bytes()
        prices = dict(re.findall(r"\|\s*`([a-z][a-z0-9_]*)`\s*\|\s*(\d+)\s*\|", canonical_bytes.decode("utf-8")))
        for name, value in contract["prices"].items():
            if prices.get(name) != str(value):
                errors.append(f"{canonical}: price {name} must equal snapshot value {value}")
    except (OSError, UnicodeError) as exc:
        canonical_bytes = None
        errors.append(f"{canonical}: cannot read shared operations contract: {exc}")
    float_canonical = root / "contracts/float.md"
    float_bytes = None
    if float_canonical.exists():
        try:
            float_bytes = float_canonical.read_bytes()
        except OSError as exc:
            errors.append(f"{float_canonical}: cannot read shared Float contract: {exc}")
    names = set()
    for folder in folders:
        skill = folder / "SKILL.md"
        try:
            text = skill.read_text(encoding="utf-8-sig")
            metadata = frontmatter(text, str(skill))
            name = metadata.get("name", "")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                errors.append(f"{skill}: invalid skill name {name!r}")
            if name != folder.name:
                errors.append(f"{skill}: name must match folder {folder.name}")
            if name in names:
                errors.append(f"{skill}: duplicate skill name {name}")
            names.add(name)
            if not metadata.get("description"):
                errors.append(f"{skill}: missing description")
            try:
                date.fromisoformat(metadata.get("last_verified", ""))
                if metadata["last_verified"] != contract["verified_at"]:
                    errors.append(f"{skill}: metadata.last_verified differs from compatibility snapshot")
            except ValueError:
                errors.append(f"{skill}: metadata.last_verified must be YYYY-MM-DD")
            if "Kolvera MCP" not in metadata.get("compatible_tools", ""):
                errors.append(f"{skill}: metadata.compatible_tools must identify Kolvera MCP")
            if not re.search(r"\[[^\]]+\]\(references/operations\.md\)", text):
                errors.append(f"{skill}: link references/operations.md for standalone safety guidance")
            reference = folder / "references/operations.md"
            if not reference.is_file() or reference.read_bytes() != canonical_bytes:
                errors.append(f"{reference}: shared operations drift; run scripts/sync_references.py --write")
            if float_bytes is not None and folder.name in {"campaign-build", "rmp-campaign"}:
                float_reference = folder / "references/float.md"
                if not float_reference.is_file() or float_reference.read_bytes() != float_bytes:
                    errors.append(f"{float_reference}: shared Float drift; run scripts/sync_references.py --write")
            for path in payload_files(folder):
                if path.suffix.lower() == ".md":
                    errors.extend(check_document(path.read_text(encoding="utf-8-sig"), path, folder, contract["tools"]))
        except (OSError, UnicodeError, ValidationError) as exc:
            errors.append(f"{skill}: {exc}")
    if errors:
        raise ValidationError("\n".join(errors))
    return contract, folders


def archive_members(path: Path) -> dict[str, bytes]:
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            if len(names) != len(set(names)):
                raise ValidationError(f"{path}: duplicate archive member")
            for name in names:
                parts = PurePosixPath(name).parts
                if not parts or name.startswith("/") or ":" in name or "\\" in name or any(p in {"..", "."} or p.startswith(".") for p in parts):
                    raise ValidationError(f"{path}: unsafe archive member {name}")
            return {name: archive.read(name) for name in names}
    except (OSError, zipfile.BadZipFile) as exc:
        raise ValidationError(f"{path}: invalid ZIP: {exc}") from exc


def validate_archives(root: Path, directory: Path, contract: dict, folders: list[Path]) -> None:
    try:
        manifest_bytes = (directory / "manifest.json").read_bytes()
        manifest = json.loads(manifest_bytes)
        expected_names = {f"{folder.name}.zip" for folder in folders}
        expected_artifacts = expected_names | {"kolvera-skills-all.zip"}
        if set(manifest["artifacts"]) != expected_artifacts:
            raise ValidationError("manifest artifact list differs from source skills")
        if manifest.get("schema_version") != 1 or manifest.get("skills") != [f.name for f in folders]:
            raise ValidationError("manifest schema or skill list mismatch")
        for key in ("verified_at", "product_source_sha"):
            if manifest.get(key) != contract[key]:
                raise ValidationError(f"manifest {key} differs from compatibility snapshot")
        if {p.name for p in directory.glob("*.zip")} != expected_artifacts:
            raise ValidationError("archive directory contains missing or unexpected ZIP files")
        checksum_lines = []
        for name in sorted(expected_artifacts):
            data = (directory / name).read_bytes()
            if manifest["artifacts"][name] != {"sha256": digest(data), "size": len(data)}:
                raise ValidationError(f"{name}: manifest checksum/size mismatch")
            checksum_lines.append(f"{digest(data)}  {name}\n")
        checksum_lines.append(f"{digest(manifest_bytes)}  manifest.json\n")
        if (directory / "CHECKSUMS.sha256").read_text(encoding="utf-8") != "".join(checksum_lines):
            raise ValidationError("CHECKSUMS.sha256 differs from generated artifacts")
        for folder in folders:
            expected = {f"{folder.name}/{path.relative_to(folder).as_posix()}": path.read_bytes() for path in payload_files(folder)}
            actual = archive_members(directory / f"{folder.name}.zip")
            if actual != expected:
                raise ValidationError(f"{folder.name}.zip: archive contents differ from standalone source payload")
            # Source reference validation plus exact byte/member comparison proves
            # each extracted standalone archive has its referenced files.
        bundle = archive_members(directory / "kolvera-skills-all.zip")
        if bundle != {name: (directory / name).read_bytes() for name in sorted(expected_names)}:
            raise ValidationError("bundle contents differ from per-skill ZIP files")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise ValidationError(f"{directory}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="source repository root")
    parser.add_argument("--archives", type=Path, help="also validate this built archive directory")
    parser.add_argument("--expected-count", type=int, help="optional release-specific skill count pin")
    args = parser.parse_args()
    try:
        contract, folders = validate_source(args.root, args.expected_count)
        if args.archives:
            validate_archives(args.root, args.archives, contract, folders)
    except ValidationError as exc:
        print(f"Validation failed:\n{exc}", file=sys.stderr)
        return 1
    print(f"Validated {len(folders)} standalone skills against offline snapshot {contract['verified_at']} ({contract['product_source_sha']}).")
    if args.archives:
        print(f"Validated ZIP payloads, manifest and SHA256 checksums in {args.archives}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())