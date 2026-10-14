"""Offline regression tests; no API calls, credentials, third-party packages or sends."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from sync_references import sync
from validate_release import ValidationError, archive_members, check_document, digest, load_contract, validate_archives, validate_source

spec = importlib.util.spec_from_file_location("release_builder", REPO / "build-release-zips.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "source"
        self.folder = self.root / "skills/example"
        (self.folder / "references").mkdir(parents=True)
        (self.root / "contracts").mkdir()
        self.contract = {
            "verified_at": "2026-10-14",
            "product_source_sha": "a" * 40,
            "prices": {"intel_report": 23, "deep_research_expand": 4},
            "tools": {
                "expand_deep_research": {"required": ["report_id"], "optional": ["focus"]},
                "create_campaign": {"required": ["name"], "optional": ["framework"]},
            },
            "notes": ["Offline compatibility fixture, not a live API check."],
        }
        (self.root / "contracts/kolvera.json").write_text(json.dumps(self.contract), encoding="utf-8")
        (self.root / "contracts/operations.md").write_text("# Operations\n\n| Key | Credits |\n|---|---|\n| `intel_report` | 23 |\n| `deep_research_expand` | 4 |\n\nSpending and outbound sends require explicit authority.\n", encoding="utf-8")
        self.skill = self.folder / "SKILL.md"
        self.skill.write_text('---\nname: example\ndescription: Test standalone workflow.\nmetadata:\n  last_verified: "2026-10-14"\n  compatible_tools: "Kolvera MCP; inspect live capabilities"\n---\n\n[Operations contract](references/operations.md)\n\nTool: `mcp__kolvera__expand_deep_research`.\nExample: `expand_deep_research(report_id=12, focus="healthcare")`.\nEnums/parameters: `tips`, `framework`, `private_draft`, `icp_id`.\n', encoding="utf-8")
        sync(self.root, write=True)
        self.output = Path(self.temporary.name) / "archives"

    def append(self, text):
        self.skill.write_text(self.skill.read_text(encoding="utf-8") + text, encoding="utf-8")

    def assert_invalid(self, message):
        with self.assertRaisesRegex(ValidationError, message):
            validate_source(self.root)

    def build(self):
        builder.build(self.root, self.output)
        return validate_source(self.root)

    def refresh_manifest(self):
        """Re-sign a malicious ZIP so payload checks cannot hide behind hash failures."""
        path = self.output / "manifest.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        for name in manifest["artifacts"]:
            data = (self.output / name).read_bytes()
            manifest["artifacts"][name] = {"sha256": digest(data), "size": len(data)}
        data = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
        path.write_bytes(data)
        checksums = "".join(f"{manifest['artifacts'][name]['sha256']}  {name}\n" for name in sorted(manifest["artifacts"]))
        (self.output / "CHECKSUMS.sha256").write_text(checksums + f"{digest(data)}  manifest.json\n", encoding="utf-8", newline="\n")

    def test_valid_source_accepts_parameters_enums_and_explicit_count_pin(self):
        contract, folders = validate_source(self.root, expected_count=1)
        self.assertEqual(contract["verified_at"], "2026-10-14")
        self.assertEqual([folder.name for folder in folders], ["example"])
        with self.assertRaisesRegex(ValidationError, "expected 18"):
            validate_source(self.root, expected_count=18)

    def test_new_legitimate_skill_needs_no_hardcoded_catalog_update(self):
        second = self.root / "skills/another"
        (second / "references").mkdir(parents=True)
        (second / "SKILL.md").write_text(self.skill.read_text(encoding="utf-8").replace("name: example", "name: another"), encoding="utf-8")
        sync(self.root, write=True)
        self.assertEqual(len(validate_source(self.root)[1]), 2)

    def test_detects_real_pre_fix_guidance_from_audited_commit(self):
        # Exact source excerpts at 30bca2a5b4adb7b0425090764e478bf492d125bc.
        excerpt = (REPO / "tests/fixtures/pre_fix_contact_excerpt.md").read_text(encoding="utf-8")
        errors = check_document(excerpt, self.skill, self.folder, self.contract["tools"])
        self.assertTrue(any("unsafe stalled-batch" in error for error in errors), errors)
        self.assertTrue(any("unsafe fresh-chat" in error for error in errors), errors)
        self.assertTrue(any("GUIDELINES.md" in error for error in errors), errors)

    def test_new_unsupported_tool_mutation_rejected(self):
        self.append("\nCall `mcp__kolvera__send_campaign_without_approval`.\n")
        self.assert_invalid("unsupported declared tool.*send_campaign_without_approval")

    def test_unknown_bare_backticked_tool_token_rejected(self):
        self.append("\nUse `get_nonexistent_kolvera_thing`.\n")
        self.assert_invalid("unsupported logical tool token get_nonexistent_kolvera_thing")

    def test_unknown_bare_tool_call_rejected(self):
        self.append("\nCall get_nonexistent_kolvera_thing(record_id=12).\n")
        self.assert_invalid("unsupported logical tool call get_nonexistent_kolvera_thing")

    def test_schema_field_names_and_unprefixed_enums_not_treated_as_tools(self):
        self.contract["tools"]["create_campaign"]["optional"] += ["send_start_hour", "stop_on_reply", "review_revision"]
        (self.root / "contracts/kolvera.json").write_text(json.dumps(self.contract), encoding="utf-8")
        self.append("\nFields: `send_start_hour`, `stop_on_reply`, `review_revision`. Enums: `tips`, `float`, `private_draft`. Prose get_nonexistent_kolvera_thing is not a declared call.\n")
        validate_source(self.root)

    def test_calling_schema_field_as_tool_still_rejected(self):
        self.contract["tools"]["create_campaign"]["optional"].append("send_start_hour")
        (self.root / "contracts/kolvera.json").write_text(json.dumps(self.contract), encoding="utf-8")
        self.append("\n`send_start_hour(record_id=12)`\n")
        self.assert_invalid("unsupported logical tool call send_start_hour")

    def test_wrong_expand_identifier_rejected(self):
        self.append("\n`expand_deep_research(icp_id=12)`\n")
        self.assert_invalid("unsupported parameter icp_id")

    def test_ambiguous_positional_expand_identifier_rejected(self):
        self.append("\n`expand_deep_research(icp_id)`\n")
        self.assert_invalid("name report_id explicitly")

    def test_namespaced_call_parameters_rejected(self):
        self.append("\n`mcp__kolvera__expand_deep_research(icp_id=12)`\n")
        self.assert_invalid("unsupported parameter icp_id")

    def test_missing_required_call_parameter_rejected(self):
        self.append('\n`expand_deep_research(focus="healthcare")`\n')
        self.assert_invalid("missing required parameters.*report_id")

    def test_frontmatter_bom_and_folded_description_supported(self):
        text = self.skill.read_text(encoding="utf-8").replace("description: Test standalone workflow.", "description: >-\n  Test standalone\n  workflow.")
        self.skill.write_bytes(b"\xef\xbb\xbf" + text.encode("utf-8"))
        validate_source(self.root)

    def test_stale_metadata_verification_date_rejected(self):
        self.skill.write_text(self.skill.read_text(encoding="utf-8").replace("2026-10-14", "2026-09-01"), encoding="utf-8")
        self.assert_invalid("last_verified differs from compatibility snapshot")

    def test_missing_and_escaping_references_rejected(self):
        self.append("\n[Missing](references/missing.md) [Outside](../../contracts/operations.md)\n")
        self.assert_invalid("non-standalone reference")

    def test_hidden_reference_cannot_pass_but_disappear_from_zip(self):
        (self.folder / ".private.md").write_text("hidden", encoding="utf-8")
        self.append("\n[Hidden](.private.md)\n")
        self.assert_invalid("reference omitted from archive")

    def test_frontmatter_and_metadata_failures(self):
        text = self.skill.read_text(encoding="utf-8")
        self.skill.write_text(text.replace("name: example", "name: incorrect").replace("description: Test standalone workflow.", "description:").replace('last_verified: "2026-10-14"', 'last_verified: "tomorrow"'), encoding="utf-8")
        self.assert_invalid("name must match folder")
        self.assert_invalid("missing description")
        self.assert_invalid("last_verified must be YYYY-MM-DD")

    def test_duplicate_names_rejected(self):
        second = self.root / "skills/another"
        second.mkdir()
        (second / "SKILL.md").write_bytes(self.skill.read_bytes())
        sync(self.root, write=True)
        self.assert_invalid("duplicate skill name")

    def test_operation_reference_drift_detected_and_sync_explicit(self):
        target = self.folder / "references/operations.md"
        target.write_text("stale", encoding="utf-8")
        self.assertEqual(sync(self.root), [str(target)])
        self.assertEqual(target.read_text(encoding="utf-8"), "stale")
        self.assert_invalid("shared operations drift")
        sync(self.root, write=True)
        validate_source(self.root)

    def test_float_reference_drift_fails_check_and_source_then_explicit_write_syncs(self):
        old_folder = self.folder
        self.folder = self.root / "skills/campaign-build"
        old_folder.rename(self.folder)
        self.skill = self.folder / "SKILL.md"
        text = self.skill.read_text(encoding="utf-8").replace("name: example", "name: campaign-build")
        text += "\n[Float contract](references/float.md)\n"
        self.skill.write_text(text, encoding="utf-8")
        rmp = self.root / "skills/rmp-campaign"
        rmp.mkdir()
        (rmp / "SKILL.md").write_text(text.replace("name: campaign-build", "name: rmp-campaign"), encoding="utf-8")
        sync(self.root, write=True)  # Operations only; optional Float canonical absent.
        canonical = self.root / "contracts/float.md"
        canonical.write_bytes(b"# Float\r\n\r\nReviewed authority, privacy and launch preview.\r\n")
        targets = [self.folder / "references/float.md", rmp / "references/float.md"]
        self.assertEqual(sync(self.root), [str(target) for target in targets])
        self.assertTrue(all(not target.exists() for target in targets))
        self.assert_invalid("shared Float drift")
        sync(self.root, write=True)
        validate_source(self.root)
        for target in targets:
            with self.subTest(skill=target.parent.parent.name):
                target.write_bytes(b"stale")
                command = [sys.executable, str(REPO / "scripts/sync_references.py"), "--root", str(self.root)]
                for mode in ([], ["--check"]):
                    check = subprocess.run(command + mode, capture_output=True, text=True)
                    self.assertEqual(check.returncode, 1, check.stderr)
                    self.assertIn(str(target), check.stderr)
                    self.assertEqual(target.read_bytes(), b"stale")
                self.assert_invalid("shared Float drift")
                written = subprocess.run(command + ["--write"], capture_output=True, text=True)
                self.assertEqual(written.returncode, 0, written.stderr)
                self.assertEqual(target.read_bytes(), canonical.read_bytes())
                validate_source(self.root)

    def test_optional_float_contract_does_not_create_campaigns_or_touch_other_skills(self):
        (self.root / "contracts/float.md").write_text("# Float guidance\n", encoding="utf-8")
        self.assertEqual(sync(self.root), [])
        self.assertEqual(sync(self.root, write=True), [])
        self.assertFalse((self.folder / "references/float.md").exists())
        self.assertFalse((self.root / "skills/campaign-build").exists())
        self.assertFalse((self.root / "skills/rmp-campaign").exists())
        validate_source(self.root)

    def test_price_snapshot_mismatch_rejected(self):
        canonical = self.root / "contracts/operations.md"
        canonical.write_text(canonical.read_text(encoding="utf-8").replace("| 23 |", "| 15 |"), encoding="utf-8")
        sync(self.root, write=True)
        self.assert_invalid("price intel_report must equal snapshot value 23")

    def test_snapshot_requires_date_and_full_source_sha(self):
        path = self.root / "contracts/kolvera.json"
        self.contract["product_source_sha"] = "main"
        path.write_text(json.dumps(self.contract), encoding="utf-8")
        with self.assertRaisesRegex(ValidationError, "full lowercase SHA"):
            load_contract(self.root)

    def test_deterministic_standalone_archives_exclude_unrelated_and_cache_files(self):
        (self.root / "unrelated").mkdir()
        (self.root / "unrelated/SKILL.md").write_text("must not package", encoding="utf-8")
        for relative in (".secret", "__pycache__/compiled.pyc", "cache/transient.txt", "stray.pyc"):
            path = self.folder / relative
            path.parent.mkdir(exist_ok=True)
            path.write_text("must not package", encoding="utf-8")
        contract, folders = self.build()
        first = {p.name: p.read_bytes() for p in self.output.iterdir()}
        builder.build(self.root, self.output)
        self.assertEqual(first, {p.name: p.read_bytes() for p in self.output.iterdir()})
        self.assertEqual(set(archive_members(self.output / "example.zip")), {"example/SKILL.md", "example/references/operations.md"})
        with tempfile.TemporaryDirectory() as extracted:
            with zipfile.ZipFile(self.output / "example.zip") as archive:
                archive.extractall(extracted)
            skill = Path(extracted) / "example"
            self.assertEqual(check_document((skill / "SKILL.md").read_text(encoding="utf-8"), skill / "SKILL.md", skill, contract["tools"]), [])
        validate_archives(self.root, self.output, contract, folders)

    def test_changed_zip_fails_checksum(self):
        contract, folders = self.build()
        with (self.output / "example.zip").open("ab") as archive:
            archive.write(b"tamper")
        with self.assertRaisesRegex(ValidationError, "checksum/size mismatch"):
            validate_archives(self.root, self.output, contract, folders)

    def test_resigned_zip_missing_reference_fails_payload_check(self):
        contract, folders = self.build()
        builder.write_zip(self.output / "example.zip", {"example/SKILL.md": self.skill.read_bytes()})
        self.refresh_manifest()
        with self.assertRaisesRegex(ValidationError, "archive contents differ"):
            validate_archives(self.root, self.output, contract, folders)

    def test_zip_path_traversal_rejected_even_when_resigned(self):
        contract, folders = self.build()
        builder.write_zip(self.output / "example.zip", {"../outside.md": b"escape"})
        self.refresh_manifest()
        with self.assertRaisesRegex(ValidationError, "unsafe archive member"):
            validate_archives(self.root, self.output, contract, folders)

    def test_changed_bundle_fails_contents_even_when_resigned(self):
        contract, folders = self.build()
        builder.write_zip(self.output / "kolvera-skills-all.zip", {"example.zip": b"stale"})
        self.refresh_manifest()
        with self.assertRaisesRegex(ValidationError, "bundle contents differ"):
            validate_archives(self.root, self.output, contract, folders)

    def test_manifest_snapshot_and_checksum_mutations_rejected(self):
        contract, folders = self.build()
        path = self.output / "manifest.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["product_source_sha"] = "b" * 40
        path.write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaisesRegex(ValidationError, "manifest product_source_sha differs"):
            validate_archives(self.root, self.output, contract, folders)

    def test_unexpected_zip_fails_without_deleting_unrelated_files(self):
        self.output.mkdir()
        unrelated = self.output / "keep.zip"
        unrelated.write_bytes(b"owned by someone else")
        with self.assertRaisesRegex(ValidationError, "unexpected existing ZIPs"):
            builder.build(self.root, self.output)
        self.assertEqual(unrelated.read_bytes(), b"owned by someone else")

    def test_build_cannot_overwrite_source(self):
        with self.assertRaisesRegex(ValidationError, "must not overwrite source"):
            builder.build(self.root, self.folder / "dist")

    def test_cli_accepts_source_and_archive_paths_and_reports_errors(self):
        self.build()
        command = [sys.executable, str(REPO / "scripts/validate_release.py"), "--root", str(self.root), "--archives", str(self.output)]
        success = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertIn("offline snapshot", success.stdout)
        self.append("\n`mcp__kolvera__not_supported`\n")
        failure = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(failure.returncode, 1)
        self.assertIn("unsupported declared tool", failure.stderr)


if __name__ == "__main__":
    unittest.main()