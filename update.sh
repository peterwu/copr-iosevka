#!/bin/bash

author="Peter Wu"
old_version=33.3.5
new_version=33.3.6

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
