%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-fonts-all
Version:        4.0.0
Release:        1%{?dist}
Summary:        Slender typeface for code, from code.

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/v%{version}.tar.gz

BuildArch:      noarch

Requires:       iosevka-fonts
Requires:       iosevka-term-fonts
Requires:       iosevka-fixed-fonts

Requires:       iosevka-slab-fonts
Requires:       iosevka-term-slab-fonts
Requires:       iosevka-fixed-slab-fonts

Requires:       iosevka-curly-fonts
Requires:       iosevka-term-curly-fonts
Requires:       iosevka-fixed-curly-fonts

Requires:       iosevka-curly-slab-fonts
Requires:       iosevka-term-curly-slab-fonts
Requires:       iosevka-fixed-curly-slab-fonts

Requires:       iosevka-ss01-fonts
Requires:       iosevka-ss02-fonts
Requires:       iosevka-ss03-fonts
Requires:       iosevka-ss04-fonts
Requires:       iosevka-ss05-fonts
Requires:       iosevka-ss06-fonts
Requires:       iosevka-ss07-fonts
Requires:       iosevka-ss08-fonts
Requires:       iosevka-ss09-fonts
Requires:       iosevka-ss10-fonts
Requires:       iosevka-ss11-fonts
Requires:       iosevka-ss12-fonts
Requires:       iosevka-ss13-fonts
Requires:       iosevka-ss14-fonts

Requires:       iosevka-term-ss01-fonts
Requires:       iosevka-term-ss02-fonts
Requires:       iosevka-term-ss03-fonts
Requires:       iosevka-term-ss04-fonts
Requires:       iosevka-term-ss05-fonts
Requires:       iosevka-term-ss06-fonts
Requires:       iosevka-term-ss07-fonts
Requires:       iosevka-term-ss08-fonts
Requires:       iosevka-term-ss09-fonts
Requires:       iosevka-term-ss10-fonts
Requires:       iosevka-term-ss11-fonts
Requires:       iosevka-term-ss12-fonts
Requires:       iosevka-term-ss13-fonts
Requires:       iosevka-term-ss14-fonts

Requires:       iosevka-fixed-ss01-fonts
Requires:       iosevka-fixed-ss02-fonts
Requires:       iosevka-fixed-ss03-fonts
Requires:       iosevka-fixed-ss04-fonts
Requires:       iosevka-fixed-ss05-fonts
Requires:       iosevka-fixed-ss06-fonts
Requires:       iosevka-fixed-ss07-fonts
Requires:       iosevka-fixed-ss08-fonts
Requires:       iosevka-fixed-ss09-fonts
Requires:       iosevka-fixed-ss10-fonts
Requires:       iosevka-fixed-ss11-fonts
Requires:       iosevka-fixed-ss12-fonts
Requires:       iosevka-fixed-ss13-fonts
Requires:       iosevka-fixed-ss14-fonts

Requires:       iosevka-aile-fonts
Requires:       iosevka-etoile-fonts
Requires:       iosevka-sparkle-fonts

%description
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.

%changelog
* Thu Nov 26 14:40:59 EST 2020 Peter Wu <peterwu@hotmail.com>
- Release v4.0.0
