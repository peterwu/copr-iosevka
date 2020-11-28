%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss14
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

# Iosevka SS14 — Monospace, JetBrains Mono Style
%package -n iosevka-ss14-fonts
Summary:        Monospace, JetBrains Mono Style
%description -n iosevka-ss14-fonts
Iosevka Monospace, JetBrains Mono Style

%package -n iosevka-term-ss14-fonts
Summary:        Monospace, JetBrains Mono Style
%description -n iosevka-term-ss14-fonts
Iosevka Monospace, JetBrains Mono Style

%package -n iosevka-fixed-ss14-fonts
Summary:        Monospace, JetBrains Mono Style
%description -n iosevka-fixed-ss14-fonts
Iosevka Monospace, JetBrains Mono Style

%build
npm install

npm run build -- ttf::iosevka-ss14
npm run build -- ttf::iosevka-term-ss14
npm run build -- ttf::iosevka-fixed-ss14

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss14/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss14-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss14/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss14-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss14/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss14-fonts

# Iosevka SS14 — Monospace, JetBrains Mono Style
%files -n iosevka-ss14-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss14-fonts/*

%files -n iosevka-term-ss14-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss14-fonts/*

%files -n iosevka-fixed-ss14-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss14-fonts/*

%changelog
* Thu Nov 26 14:40:59 EST 2020 Peter Wu <peterwu@hotmail.com>
- Release v4.0.0
