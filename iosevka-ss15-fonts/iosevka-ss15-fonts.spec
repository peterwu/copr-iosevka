%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss15
Version:        5.0.3
Release:        1%{?dist}
Summary:        Slender typeface for code, from code.

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  clang
BuildRequires:  npm
BuildRequires:  ttfautohint

%description
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.

%prep
%autosetup -n %{source_name}-%{version}

# Iosevka SS15 — Monospace, IBM Plex Mono Style
%package -n iosevka-ss15-fonts
Summary:        Monospace, IBM Plex Mono Style
%description -n iosevka-ss15-fonts
Iosevka Monospace, IBM Plex Mono Style

%package -n iosevka-term-ss15-fonts
Summary:        Monospace, IBM Plex Mono Style
%description -n iosevka-term-ss15-fonts
Iosevka Monospace, IBM Plex Mono Style

%package -n iosevka-fixed-ss15-fonts
Summary:        Monospace, IBM Plex Mono Style
%description -n iosevka-fixed-ss15-fonts
Iosevka Monospace, IBM Plex Mono Style

%build
npm install

npm run build -- ttf::iosevka-ss15
npm run build -- ttf::iosevka-term-ss15
npm run build -- ttf::iosevka-fixed-ss15

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss15/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss15-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss15/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss15-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss15/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss15-fonts

# Iosevka SS15 — Monospace, IBM Plex Mono Style
%files -n iosevka-ss15-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss15-fonts/*

%files -n iosevka-term-ss15-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss15-fonts/*

%files -n iosevka-fixed-ss15-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss15-fonts/*

%changelog
* Sat Feb 20 16:29:32 EST 2021 Peter Wu - v5.0.3
- Release v5.0.3
* Wed Feb 17 09:20:02 EST 2021 Peter Wu - v5.0.2
- Release v5.0.2
* Sun Feb 14 11:13:38 EST 2021 Peter Wu - v5.0.1
- Release v5.0.1
* Sat Feb 13 09:54:24 EST 2021 Peter Wu - v5.0.0
- Release v5.0.0
