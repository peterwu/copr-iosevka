#!/usr/bin/env python3
"""Release Iosevka COPR packages: update version, commit, push, and submit builds."""

import argparse
import re
import subprocess
from datetime import datetime
from pathlib import Path

from copr.v3 import Client
from copr.v3.exceptions import CoprRequestException

AUTHOR     = "Peter Wu"
CLONE_URL  = "https://github.com/peterwu/copr-iosevka.git"
COMMITTISH = "main"
TIMEOUT    = 58000
COPR_REPO  = "peterwu/iosevka"

FONTS = [
    "iosevka",
    "iosevka-slab",
    "iosevka-curly",
    "iosevka-curly-slab",
    "iosevka-ss01",
    "iosevka-ss02",
    "iosevka-ss03",
    "iosevka-ss04",
    "iosevka-ss05",
    "iosevka-ss06",
    "iosevka-ss07",
    "iosevka-ss08",
    "iosevka-ss09",
    "iosevka-ss10",
    "iosevka-ss11",
    "iosevka-ss12",
    "iosevka-ss13",
    "iosevka-ss14",
    "iosevka-ss15",
    "iosevka-ss16",
    "iosevka-ss17",
    "iosevka-ss18",
    "iosevka-aile",
    "iosevka-etoile",
]


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Release Iosevka COPR packages")
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
    return f"* {today} {AUTHOR} - v{version}\n- Release v{version}"


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


def update_specs(new_release):
    """Update all .spec files to the new release version."""
    spec_files = list(Path(".").rglob("*.spec"))
    if not spec_files:
        raise FileNotFoundError("No .spec files found")

    old_release = get_current_version(spec_files[0])
    entry = make_entry(new_release)

    for spec_file in spec_files:
        update_spec(spec_file, old_release, new_release, entry)
        print(f"  Updated: {spec_file}")

    return spec_files


def git_commit_and_push(spec_files, new_release):
    """Stage modified .spec files, commit, and push."""
    for spec_file in spec_files:
        subprocess.run(["git", "add", str(spec_file)], check=True)

    subprocess.run(
        ["git", "commit", "-m", f"update to v{new_release}"],
        check=True,
    )
    subprocess.run(["git", "push"], check=True)


def submit_build(client, owner, project, font):
    """Submit a COPR SCM build for a single font variant."""
    return client.build_proxy.create_from_scm(
        ownername    = owner,
        projectname  = project,
        clone_url    = CLONE_URL,
        committish   = COMMITTISH,
        subdirectory = f"{font}-fonts",
        spec         = f"{font}-fonts.spec",
        buildopts    = {
            "timeout":    TIMEOUT,
            "enable_net": True,
            "background": True,
        },
    )


def submit_builds():
    """Submit COPR builds for all font variants."""
    owner, project = COPR_REPO.split("/")
    client = Client.create_from_config_file()

    for font in FONTS:
        print(f"  Submitting build for {font}...")
        try:
            build = submit_build(client, owner, project, font)
            print(f"    Build {build.id} submitted")
        except CoprRequestException as e:
            print(f"    Failed: {e}")
            raise


def main():
    """Entry point."""
    args = parse_args()
    new_release = args.release

    print(f"==> Updating .spec files to v{new_release}...")
    spec_files = update_specs(new_release)

    print("==> Committing and pushing...")
    git_commit_and_push(spec_files, new_release)

    print("==> Submitting COPR builds...")
    submit_builds()

    print("==> Done.")


if __name__ == "__main__":
    main()

