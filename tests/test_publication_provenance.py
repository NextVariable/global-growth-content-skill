"""Verify integrity and publication checks, without grading generated content."""

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validation", ROOT / "scripts/validate.py")
VALIDATION = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATION)


class PublicationChecks(unittest.TestCase):
    def test_public_copy_does_not_replace_original_hash(self):
        original, published = b"original locator", b"public locator"
        original_hash = hashlib.sha256(original).hexdigest()
        public_hash = hashlib.sha256(published).hexdigest()
        export = {"asset.md": {"original_sha256": original_hash, "published_sha256": public_hash}}
        self.assertTrue(VALIDATION.digest_matches(published, original_hash, "asset.md", export))
        self.assertFalse(VALIDATION.digest_matches(published, public_hash, "asset.md", export))
        self.assertFalse(
            VALIDATION.digest_matches(published + b"edit", original_hash, "asset.md", export)
        )

    def test_unexported_bytes_are_not_normalised(self):
        data = b"record\n"
        digest = hashlib.sha256(data).hexdigest()
        self.assertTrue(VALIDATION.digest_matches(data, digest, "asset.md", {}))
        self.assertFalse(VALIDATION.digest_matches(b"record\r\n", digest, "asset.md", {}))

    def test_public_candidate_checked_and_private_archive_ignored(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / ".gitignore").write_text("local-audits/\n", encoding="utf-8")
            locator = "/".join(["", "home", "test-person", "private-record"])
            (root / "candidate.md").write_text(locator, encoding="utf-8")
            archive = root / "local-audits"
            archive.mkdir()
            (archive / "original.md").write_text(locator, encoding="utf-8")
            self.assertEqual(
                VALIDATION.publication_errors(root),
                ["personal filesystem locator: candidate.md"],
            )

    def test_modified_public_export_is_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            validation = root / "validation"
            validation.mkdir()
            asset = root / "asset.md"
            asset.write_bytes(b"published")
            export = {
                "files": {
                    "asset.md": {
                        "original_sha256": hashlib.sha256(b"private original").hexdigest(),
                        "published_sha256": hashlib.sha256(asset.read_bytes()).hexdigest(),
                    }
                }
            }
            (validation / "public-export.json").write_text(json.dumps(export), encoding="utf-8")
            self.assertEqual(VALIDATION.publication_errors(root), [])
            asset.write_bytes(b"changed after export")
            self.assertEqual(
                VALIDATION.publication_errors(root), ["published copy changed: asset.md"]
            )


if __name__ == "__main__":
    unittest.main()
