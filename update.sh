#!/bin/bash

author="Peter Wu"
old_version=34.2.1
new_version=34.3.0

today=$(date "+%a %b %d %T %Z %Y")
content="Release v${new_version}"

entry="* ${today} ${author} - v${new_version}"
entry+="\n"
entry+="- ${content}"

find . -type f -name '*.spec' | while IFS= read -r file; do
    awk -v old="${old_version}" \
        -v new="${new_version}" \
        -v entry="${entry}"     \
    '
        /Version:/ { sub(old, new) }
        /^%changelog/ { print; print entry; next }
        { print }
    ' "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
done
