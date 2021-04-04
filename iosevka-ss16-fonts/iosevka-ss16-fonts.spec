%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss16
Version:        5.2.1
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
* Sun Apr 04 09:34:28 EDT 2021 Peter Wu - v5.2.1
- Release v5.2.1
* Sat Apr 03 12:18:18 EDT 2021 Peter Wu - v5.2.0
- Release v5.2.0
* Sun Mar 28 19:26:33 EDT 2021 Peter Wu - v5.1.1
- Release v5.1.1
* Sat Mar 27 10:53:10 EDT 2021 Peter Wu - v5.1.0
- Release v5.1.0
* Mon Mar 22 09:33:49 EDT 2021 Peter Wu - v5.0.9
- Release v5.0.9
* Sun Mar 14 20:17:31 EDT 2021 Peter Wu - v5.0.8
- Release v5.0.8
* Sat Mar 13 18:47:27 EST 2021 Peter Wu - v5.0.6
- Release v5.0.6
* Sat Mar 06 09:55:14 EST 2021 Peter Wu - v5.0.5
- Release v5.0.5
* Sat Feb 27 15:47:08 EST 2021 Peter Wu - v5.0.4
- Release v5.0.4
* Sat Feb 20 16:29:32 EST 2021 Peter Wu - v5.0.3
- Release v5.0.3
* Wed Feb 17 09:20:02 EST 2021 Peter Wu - v5.0.2
- Release v5.0.2
* Sun Feb 14 11:13:38 EST 2021 Peter Wu - v5.0.1
- Release v5.0.1
* Sat Feb 13 09:54:24 EST 2021 Peter Wu - v5.0.0
- Release v5.0.0
