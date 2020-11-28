%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-aile
Version:        4.0.0
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

# Iosevka Aile — Quasi-proportional, Sans-serif
%package -n iosevka-aile-fonts
Summary:        Quasi-proportional, Sans-serif
%description -n iosevka-aile-fonts
Iosevka Quasi-proportional, Sans-serif

%build
npm install

npm run build -- ttf::iosevka-aile

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-aile/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-aile-fonts


# Iosevka Aile — Quasi-proportional, Sans-serif
%files -n iosevka-aile-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-aile-fonts/*

%changelog
* Thu Nov 26 14:40:59 EST 2020 Peter Wu <peterwu@hotmail.com>
- Release v4.0.0
