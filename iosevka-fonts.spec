%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka
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

# Iosevka — Monospace, Default
%package -n iosevka-fonts
Summary:        Monospace, Default
%description -n iosevka-fonts
Iosevka Monospace, Default

%package -n iosevka-term-fonts
Summary:        Monospace, Default
%description -n iosevka-term-fonts
Iosevka Monospace, Default

%package -n iosevka-fixed-fonts
Summary:        Monospace, Default
%description -n iosevka-fixed-fonts
Iosevka Monospace, Default

%build
npm install
npm run build -- ttf::iosevka
npm run build -- ttf::iosevka-term
npm run build -- ttf::iosevka-fixed

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-fonts

# Iosevka — Monospace, Default
%files -n iosevka-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fonts/*

%files -n iosevka-term-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-fonts/*

%files -n iosevka-fixed-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-fonts/*

%changelog
* Thu Nov 26 14:40:59 EST 2020 Peter Wu <peterwu@hotmail.com>
- Release v4.0.0
