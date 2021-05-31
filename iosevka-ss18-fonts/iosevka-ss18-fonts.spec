%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss18
Version:        7.0.2
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

# Iosevka SS18 — Monospace, Input Mono Style
%package -n iosevka-ss18-fonts
Summary:        Monospace, Input Mono Style
%description -n iosevka-ss18-fonts
Iosevka Monospace, Input Mono Style

%package -n iosevka-term-ss18-fonts
Summary:        Monospace, Input Mono Style
%description -n iosevka-term-ss18-fonts
Iosevka Monospace, Input Mono Style

%package -n iosevka-fixed-ss18-fonts
Summary:        Monospace, Input Mono Style
%description -n iosevka-fixed-ss18-fonts
Iosevka Monospace, Input Mono Style

%build
npm install

npm run build -- ttf::iosevka-ss18
npm run build -- ttf::iosevka-term-ss18
npm run build -- ttf::iosevka-fixed-ss18

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss18/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss18-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss18/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss18-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss18/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss18-fonts

# Iosevka SS18 — Monospace, Input Mono Style
%files -n iosevka-ss18-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss18-fonts/*

%files -n iosevka-term-ss18-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss18-fonts/*

%files -n iosevka-fixed-ss18-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss18-fonts/*

%changelog
* Mon May 31 09:47:01 EDT 2021 Peter Wu - v7.0.2
- Release v7.0.2
* Sun May 30 10:03:54 EDT 2021 Peter Wu - v7.0.1
- Release v7.0.1
* Sat May 29 10:15:05 EDT 2021 Peter Wu - v7.0.0
- Release v7.0.0