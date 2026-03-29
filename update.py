#!/usr/bin/env python3

import re
from datetime import datetime
from pathlib import Path

AUTHOR      = "Peter Wu"
OLD_VERSION = "34.2.1"
NEW_VERSION = "34.3.0"

today   = datetime.now().astimezone().strftime("%a %b %d %H:%M:%S %Z %Y")
content = f"Release v{NEW_VERSION}"
entry   = f"* {today} {AUTHOR} - v{NEW_VERSION}\n- {content}"

for spec_file in Path(".").rglob("*.spec"):
    lines = spec_file.read_text().splitlines()
    output = []
    for line in lines:
        if line.startswith("Version:"):
            line = line.replace(OLD_VERSION, NEW_VERSION)
        if re.match(r"^%changelog", line):
            output.append(line)
            output.append(entry)
            continue
        output.append(line)
    spec_file.write_text("\n".join(output) + "\n")
