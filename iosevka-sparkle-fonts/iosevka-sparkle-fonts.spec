%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-sparkle
Version:        4.0.1
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

# Iosevka Sparkle — Quasi-proportional, Hybrid, like iA Writer’s Duo
%package -n iosevka-sparkle-fonts
Summary:        Quasi-proportional, Hybrid, like iA Writer’s Duo
%description -n iosevka-sparkle-fonts
Iosevka Quasi-proportional, Hybrid, like iA Writer’s Duo

%build
npm install

npm run build -- ttf::iosevka-sparkle

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-sparkle/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-sparkle-fonts

# Iosevka Sparkle — Quasi-proportional, Hybrid, like iA Writer’s Duo
%files -n iosevka-sparkle-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-sparkle-fonts/*

%changelog
* Sat Dec 05 10:18:42 EST 2020 Peter Wu - v4.0.1
- Release v4.0.1
* Thu Nov 26 14:40:59 EST 2020 Peter Wu <peterwu@hotmail.com>
- Release v4.0.0
