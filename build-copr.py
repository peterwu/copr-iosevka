#!/usr/bin/env python3

from copr.v3 import Client
from copr.v3.exceptions import CoprRequestException

CLONE_URL  = "https://github.com/peterwu/copr-iosevka.git"
COMMITTISH = "main"
TIMEOUT    = 58000
COPR_REPO  = "peterwu/iosevka"

OWNER, PROJECT = COPR_REPO.split("/")

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

client = Client.create_from_config_file()

for font in FONTS:
    print(f"Submitting build for {font}...")
    try:
        build = client.build_proxy.create_from_scm(
            ownername    = OWNER,
            projectname  = PROJECT,
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
        print(f"  Build {build.id} submitted")
    except CoprRequestException as e:
        print(f"  Failed: {e}")
        raise
