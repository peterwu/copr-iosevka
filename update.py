#!/usr/bin/env python3
"""Update version and changelog in RPM .spec files."""

import re
import argparse
from datetime import datetime
from pathlib import Path

AUTHOR = "Peter Wu"


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Update version in .spec files")
    parser.add_argument(
        "-r", "--release", metavar="VERSION", required=True, help="New release version"
    )
    return parser.parse_args()


def get_current_version(spec_file):
    """Read the current Version: field from a .spec file."""
    for line in spec_file.read_text().splitlines():
        if line.startswith("Version:"):
            return line.split()[-1]
    raise ValueError(f"No Version: field found in {spec_file}")


def make_entry(version):
    """Build a changelog entry for the given version."""
    today = datetime.now().astimezone().strftime("%a %b %d %H:%M:%S %Z %Y")
    content = f"Release v{version}"
    return f"* {today} {AUTHOR} - v{version}\n- {content}"


def update_spec(spec_file, old_release, new_release, entry):
    """Update version and prepend changelog entry in a .spec file."""
    lines = spec_file.read_text().splitlines()
    output = []
    for line in lines:
        if line.startswith("Version:"):
            line = line.replace(old_release, new_release)
        if re.match(r"^%changelog", line):
            output.append(line)
            output.append(entry)
            continue
        output.append(line)
    spec_file.write_text("\n".join(output) + "\n")


def main():
    """Entry point."""
    args = parse_args()
    new_release = args.release

    spec_files = list(Path(".").rglob("*.spec"))
    if not spec_files:
        print("No .spec files found")
        raise SystemExit(1)

    old_release = get_current_version(spec_files[0])
    entry = make_entry(new_release)

    for spec_file in spec_files:
        update_spec(spec_file, old_release, new_release, entry)
        print(f"Updated: {spec_file}")


if __name__ == "__main__":
    main()
