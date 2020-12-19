#!/bin/bash

author="Peter Wu"
old_version=4.0.3
new_version=4.1.0

today=$(date "+%a %b %d %T %Z %Y")
content="Release v${new_version}"

entry="* ${today} ${author} - v${new_version}"
entry+="\n"
entry+="- ${content}"

find . -type f -name '*.spec' -exec sed -i -e "1,9 s/${old_version}/${new_version}/" -e '/%changelog/a\' -e "${entry}" {} \;
