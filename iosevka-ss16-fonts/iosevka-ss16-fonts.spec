%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss16
Version:        5.0.0
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

# Iosevka SS16 — Monospace, PT Mono Style
%package -n iosevka-ss16-fonts
Summary:        Monospace, PT Mono Style
%description -n iosevka-ss16-fonts
Iosevka Monospace, PT Mono Style

%package -n iosevka-term-ss16-fonts
Summary:        Monospace, PT Mono Style
%description -n iosevka-term-ss16-fonts
Iosevka Monospace, PT Mono Style

%package -n iosevka-fixed-ss16-fonts
Summary:        Monospace, PT Mono Style
%description -n iosevka-fixed-ss16-fonts
Iosevka Monospace, PT Mono Style

%build
npm install

npm run build -- ttf::iosevka-ss16
npm run build -- ttf::iosevka-term-ss16
npm run build -- ttf::iosevka-fixed-ss16

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss16/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss16-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss16/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss16-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss16/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss16-fonts

# Iosevka SS16 — Monospace, PT Mono Style
%files -n iosevka-ss16-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss16-fonts/*

%files -n iosevka-term-ss16-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss16-fonts/*

%files -n iosevka-fixed-ss16-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss16-fonts/*

%changelog
* Sat Feb 13 09:54:24 EST 2021 Peter Wu - v5.0.0
- Release v5.0.0
