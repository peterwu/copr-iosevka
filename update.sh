#!/bin/bash

author="Peter Wu"
old_version=34.2.1
new_version=34.3.0

today=$(date "+%a %b %d %T %Z %Y")
content="Release v${new_version}"

entry="* ${today} ${author} - v${new_version}"
entry+="\n"
entry+="- ${content}"

case "$OSTYPE" in
    darwin*)
        PREFIX="g"
        ;;
    *)
        PREFIX=""
        ;;
esac

SED="${PREFIX}sed"

find . -type f -name '*.spec' -exec ${SED} -i       \
    -e "/Version:/s/${old_version}/${new_version}/" \
    -e "/%changelog/a ${entry}" {} \;
