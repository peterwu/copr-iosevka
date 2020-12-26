%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss05
Version:        4.2.0
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

# Iosevka SS05 — Monospace, Fira Mono Style
%package -n iosevka-ss05-fonts
Summary:        Monospace, Fira Mono Style
%description -n iosevka-ss05-fonts
Iosevka Monospace, Fira Mono Style

%package -n iosevka-term-ss05-fonts
Summary:        Monospace, Fira Mono Style
%description -n iosevka-term-ss05-fonts
Iosevka Monospace, Fira Mono Style

%package -n iosevka-fixed-ss05-fonts
Summary:        Monospace, Fira Mono Style
%description -n iosevka-fixed-ss05-fonts
Iosevka Monospace, Fira Mono Style

%build
npm install

npm run build -- ttf::iosevka-ss05
npm run build -- ttf::iosevka-term-ss05
npm run build -- ttf::iosevka-fixed-ss05

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss05/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss05-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss05/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss05-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss05/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss05-fonts

# Iosevka SS05 — Monospace, Fira Mono Style
%files -n iosevka-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss05-fonts/*

%files -n iosevka-term-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss05-fonts/*

%files -n iosevka-fixed-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss05-fonts/*

%changelog
* Sat Dec 26 09:19:12 EST 2020 Peter Wu - v4.2.0
- Release v4.2.0
* Sat Dec 19 18:01:02 EST 2020 Peter Wu - v4.1.1
- Release v4.1.1
* Sat Dec 19 09:06:44 EST 2020 Peter Wu - v4.1.0
- Release v4.1.0
* Sat Dec 12 09:28:44 EST 2020 Peter Wu - v4.0.3
- Release v4.0.3
* Sun Dec 06 10:38:56 EST 2020 Peter Wu - v4.0.2
- Release v4.0.2
* Sat Dec 05 10:18:42 EST 2020 Peter Wu - v4.0.1
- Release v4.0.1
* Thu Nov 26 14:40:59 EST 2020 Peter Wu <peterwu@hotmail.com>
- Release v4.0.0
