#!/usr/bin/env python3
"""Check the portable skill package and reproducible task-test provenance.

This does not grade writing, assert real customer outcomes, or call a model.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/global-growth-content"


def publication_export(root):
    path = root / "validation/public-export.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def digest_matches(data, original_digest, key, exported_records):
    """Keep the recorded model hash; check a disclosed public copy separately."""
    current_digest = hashlib.sha256(data).hexdigest()
    export = exported_records.get(key)
    if export:
        return (
            original_digest == export["original_sha256"]
            and current_digest == export["published_sha256"]
        )
    return current_digest == original_digest


def package_errors(skill):
    errors = []
    entry = skill / "SKILL.md"
    if not entry.is_file():
        return ["missing SKILL.md"]
    text = entry.read_text(encoding="utf-8")
    front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    fields = dict(re.findall(r"^(name|description):\s*(.+)$", front[1], re.M)) if front else {}
    if fields.get("name") != "global-growth-content":
        errors.append("frontmatter name mismatch")
    if not 0 < len(fields.get("description", "")) <= 1024:
        errors.append("missing or oversized description")
    for path in sorted(skill.rglob("*")):
        if path.is_symlink():
            errors.append(f"symlink in install unit: {path.relative_to(skill)}")
        if not path.is_file() or path.suffix != ".md":
            continue
        content = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for link in re.findall(r"\[[^\]\n]+\]\(([^)]+)\)", content):
            target = link.split("#", 1)[0].strip("<>")
            if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue
            destination = (path.parent / target).resolve()
            if not destination.is_relative_to(skill.resolve()):
                errors.append(f"install unit depends on outside path: {target}")
            elif not destination.exists():
                errors.append(f"broken local link: {target}")
    return errors


def provenance_errors(root):
    """Compare inputs, not output wording or marketing quality."""
    fixture = json.loads((root / "tests/fixtures/cases.json").read_text(encoding="utf-8"))
    cases = {case["id"]: case for case in fixture["cases"]}
    errors = []
    exports = publication_export(root)
    if len(cases) != len(fixture["cases"]):
        errors.append("duplicate case IDs")
    runs = (
        ("baseline", cases),
        ("skill-v1", cases),
        (
            "skill-v2",
            {
                key: cases[key]
                for key in (
                    "b2b-new",
                    "conflicting-handoff",
                    "multilingual",
                    "hardware-subscription",
                )
            },
        ),
        ("skill-v3", {"multilingual": cases["multilingual"]}),
        (
            "followup",
            {
                case["id"]: case
                for case in json.loads(
                    (root / "tests/fixtures/followup-cases.json").read_text(encoding="utf-8")
                )["cases"]
            },
        ),
    )
    for mode, expected_cases in runs:
        path = root / "validation" / mode / "manifest.json"
        if not path.is_file():
            errors.append(f"missing raw-run manifest: {mode}")
            continue
        manifest = json.loads(path.read_text(encoding="utf-8"))
        records = manifest.get("cases", [])
        if {record["id"] for record in records} != set(expected_cases) or len(records) != len(
            expected_cases
        ):
            errors.append(f"case coverage differs: {mode}")
        for record in records:
            case_id = record["id"]
            if case_id not in expected_cases:
                continue
            fixture_name = "followup-cases.json" if mode == "followup" else "cases.json"
            if not digest_matches(
                expected_cases[case_id]["input"].encode(),
                record.get("input_sha256"),
                f"tests/fixtures/{fixture_name}#{case_id}",
                exports.get("inputs", {}),
            ):
                errors.append(f"input differs: {mode}/{case_id}")
            output = root / "validation" / mode / f"{case_id}.md"
            if not output.is_file() or not output.read_text(encoding="utf-8").strip():
                errors.append(f"missing actual output: {mode}/{case_id}")
            elif not digest_matches(
                output.read_bytes(),
                record.get("output_sha256"),
                output.relative_to(root).as_posix(),
                exports.get("files", {}),
            ):
                errors.append(f"raw output changed or hash missing: {mode}/{case_id}")
    return errors


def run(output):
    output.mkdir(parents=True, exist_ok=True)
    checks = []
    for name, function, argument in (
        ("portable-package", package_errors, SKILL),
        ("task-provenance", provenance_errors, ROOT),
        ("content-audit-provenance", content_audit_errors, ROOT),
        ("publication-safety", publication_errors, ROOT),
    ):
        try:
            errors = function(argument)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors = [str(exc)]
        checks.append({"name": name, "passed": not errors, "errors": errors})
    report = {
        "passed": all(check["passed"] for check in checks),
        "checks": checks,
        "limits": "Package and provenance checks only; see human semantic review separately. "
        "Synthetic tasks are not customer comprehension, channel delivery or growth evidence.",
    }
    (output / "summary.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return report


def content_audit_errors(root):
    """Validate saved model-run inputs and raw outputs, never their quality."""
    fixture = json.loads((root / "tests/fixtures/content-audit.json").read_text(encoding="utf-8"))
    cases = {case["id"]: case for case in fixture["cases"]}
    update = {fixture["updates"]["id"]: fixture["updates"]}
    audit = root / "validation/model-audit-80a2870"
    retest = json.loads((audit / "retest-input.json").read_text(encoding="utf-8"))
    rerun_cases = {case["id"]: case for case in retest["cases"]}
    runs = [(group, cases) for group in ("ordinary", "gingiris", "ours-before")]
    runs += [(group + "-update", update) for group in ("ordinary", "gingiris", "ours-before")]
    runs += [("ours-after", rerun_cases)]
    followup = json.loads((audit / "retest-update-input.json").read_text(encoding="utf-8"))
    runs += [("ours-after-update", {followup["id"]: followup})]
    runs += [("routing-retest", {"local-rewrite": cases["local-rewrite"]})]
    errors = []
    exports = publication_export(root)
    for group, expected in runs:
        manifest = json.loads((audit / group / "manifest.json").read_text(encoding="utf-8"))
        records = manifest["cases"] if "cases" in manifest else [manifest]
        if len(records) != len(expected) or {r["id"] for r in records} != set(expected):
            errors.append(f"audit case coverage differs: {group}")
        for record in records:
            case_id = record["id"]
            if case_id not in expected:
                continue
            fixture_name = "tests/fixtures/content-audit.json"
            if group == "ours-after":
                fixture_name = "validation/model-audit-80a2870/retest-input.json"
            elif group == "ours-after-update":
                fixture_name = "validation/model-audit-80a2870/retest-update-input.json"
            if not digest_matches(
                expected[case_id]["input"].encode(),
                record.get("input_sha256"),
                f"{fixture_name}#{case_id}",
                exports.get("inputs", {}),
            ):
                errors.append(f"audit input differs: {group}/{case_id}")
            output = audit / group / f"{case_id}.md"
            if not output.is_file() or not output.read_text(encoding="utf-8").strip():
                errors.append(f"missing audit output: {group}/{case_id}")
            elif not digest_matches(
                output.read_bytes(),
                record.get("output_sha256"),
                output.relative_to(root).as_posix(),
                exports.get("files", {}),
            ):
                errors.append(f"audit raw output changed: {group}/{case_id}")
    return errors


def publication_errors(root):
    """Check public files, not ignored original archives or content quality."""
    errors = []
    exports = publication_export(root)
    for name, record in exports.get("files", {}).items():
        path = root / name
        if not path.resolve().is_relative_to(root.resolve()) or not path.is_file():
            errors.append(f"invalid publication export path: {name}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != record["published_sha256"]:
            errors.append(f"published copy changed: {name}")
    filenames = (
        subprocess.check_output(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=root,
        )
        .decode("utf-8")
        .split("\0")
    )
    home_path = re.compile(r"/(?:Users|home)/[A-Za-z0-9_.-]+/|[A-Za-z]:\\Users\\[A-Za-z0-9_.-]+\\")
    email = re.compile(r"[\w.+-]+@([\w.-]+\.[A-Za-z]{2,})")
    credential = re.compile(
        r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[A-Z0-9]{16})\b"
    )
    for name in filter(None, filenames):
        path = root / name
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if home_path.search(content):
            errors.append(f"personal filesystem locator: {name}")
        if any(
            domain.lower() not in {"example.com", "example.org", "users.noreply.github.com"}
            for domain in email.findall(content)
        ):
            errors.append(f"non-example email in public file: {name}")
        if credential.search(content):
            errors.append(f"possible credential in public file: {name}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output:
        report = run(args.output.resolve())
    else:
        with tempfile.TemporaryDirectory(prefix="growth-content-check-") as folder:
            report = run(Path(folder))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return int(not report["passed"])


if __name__ == "__main__":
    sys.exit(main())
