#!/usr/bin/env python3
"""Check the portable skill package and reproducible task-test provenance.

This does not grade writing, assert real customer outcomes, or call a model.
"""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/global-growth-content"


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
            digest = hashlib.sha256(expected_cases[case_id]["input"].encode()).hexdigest()
            if record.get("input_sha256") != digest:
                errors.append(f"input differs: {mode}/{case_id}")
            output = root / "validation" / mode / f"{case_id}.md"
            if not output.is_file() or not output.read_text(encoding="utf-8").strip():
                errors.append(f"missing actual output: {mode}/{case_id}")
            elif record.get("output_sha256") != hashlib.sha256(output.read_bytes()).hexdigest():
                errors.append(f"raw output changed or hash missing: {mode}/{case_id}")
    return errors


def run(output):
    output.mkdir(parents=True, exist_ok=True)
    checks = []
    for name, function, argument in (
        ("portable-package", package_errors, SKILL),
        ("task-provenance", provenance_errors, ROOT),
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
