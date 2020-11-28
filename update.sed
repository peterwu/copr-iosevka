# run the following to update version and changelog
#
# find . -type f -name '*.spec' -exec sed -i -f update.sed {} \;
#

# update the version
1,9 s/4.0.0/4.0.1/

# add a new change log
/%changelog/a \
* Sat Nov 28 03:14:54 PM EST 2020 Peter Wu - v4.0.1\
- Release v4.0.1
