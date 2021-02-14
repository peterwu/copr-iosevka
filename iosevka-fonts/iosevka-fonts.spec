%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka
Version:        5.0.1
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
* Sun Feb 14 11:13:38 EST 2021 Peter Wu - v5.0.1
- Release v5.0.1
* Sat Feb 13 09:54:24 EST 2021 Peter Wu - v5.0.0
- Release v5.0.0
* Sat Jan 16 09:19:10 EST 2021 Peter Wu - v4.5.0
- Release v4.5.0
* Sat Jan 09 09:14:30 EST 2021 Peter Wu - v4.4.0
- Release v4.4.0
* Sat Jan 02 13:23:06 EST 2021 Peter Wu - v4.3.0
- Release v4.3.0
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
