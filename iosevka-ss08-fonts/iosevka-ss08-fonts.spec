%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss08
Version:        7.3.3
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

# Iosevka SS08 — Monospace, Pragmata Pro Style
%package -n iosevka-ss08-fonts
Summary:        Monospace, Pragmata Pro Style
%description -n iosevka-ss08-fonts
Iosevka Monospace, Monaco Style

%package -n iosevka-term-ss08-fonts
Summary:        Monospace, Pragmata Pro Style
%description -n iosevka-term-ss08-fonts
Iosevka Monospace, Monaco Style

%package -n iosevka-fixed-ss08-fonts
Summary:        Monospace, Pragmata Pro Style
%description -n iosevka-fixed-ss08-fonts
Iosevka Monospace, Monaco Style

%build
npm install

npm run build -- ttf::iosevka-ss08
npm run build -- ttf::iosevka-term-ss08
npm run build -- ttf::iosevka-fixed-ss08

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss08/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss08-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss08/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss08-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss08/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss08-fonts

# Iosevka SS08 — Monospace, Pragmata Pro Style
%files -n iosevka-ss08-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss08-fonts/*

%files -n iosevka-term-ss08-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss08-fonts/*

%files -n iosevka-fixed-ss08-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss08-fonts/*

%changelog
* Thu Jul 22 09:36:25 EDT 2021 Peter Wu - v7.3.3
- Release v7.3.3
* Wed Jul 21 09:48:02 EDT 2021 Peter Wu - v7.3.2
- Release v7.3.2
* Mon Jul 19 10:02:39 EDT 2021 Peter Wu - v7.3.1
- Release v7.3.1
* Sat Jul 17 09:32:47 EDT 2021 Peter Wu - v7.3.0
- Release v7.3.0
* Sun Jul 11 20:48:15 EDT 2021 Peter Wu - v7.2.8
- Release v7.2.8
* Sat Jul 10 08:37:51 EDT 2021 Peter Wu - v7.2.7
- Release v7.2.7
* Mon Jul 05 08:36:30 EDT 2021 Peter Wu - v7.2.6
- Release v7.2.6
* Sun Jul 04 11:01:39 EDT 2021 Peter Wu - v7.2.5
- Release v7.2.5
* Sat Jul 03 08:40:49 EDT 2021 Peter Wu - v7.2.4
- Release v7.2.4
* Tue Jun 29 22:02:43 EDT 2021 Peter Wu - v7.2.3
- Release v7.2.3
* Mon Jun 28 09:39:09 EDT 2021 Peter Wu - v7.2.2
- Release v7.2.2
* Sun Jun 27 09:54:50 EDT 2021 Peter Wu - v7.2.1
- Release v7.2.1
* Sat Jun 26 09:56:41 EDT 2021 Peter Wu - v7.2.0
- Release v7.2.0
* Sun Jun 20 09:32:15 EDT 2021 Peter Wu - v7.1.1
- Release v7.1.1
* Sat Jun 19 09:55:16 EDT 2021 Peter Wu - v7.1.0
- Release v7.1.0
* Mon Jun 07 09:47:05 EDT 2021 Peter Wu - v7.0.4
- Release v7.0.4
* Tue Jun 01 09:24:03 EDT 2021 Peter Wu - v7.0.3
- Release v7.0.3
* Mon May 31 09:47:01 EDT 2021 Peter Wu - v7.0.2
- Release v7.0.2
* Sun May 30 10:03:54 EDT 2021 Peter Wu - v7.0.1
- Release v7.0.1
* Sat May 29 10:15:05 EDT 2021 Peter Wu - v7.0.0
- Release v7.0.0
* Tue May 04 09:42:30 EDT 2021 Peter Wu - v6.1.3
- Release v6.1.3
* Sun May 02 09:49:48 EDT 2021 Peter Wu - v6.1.2
- Release v6.1.2
* Sat May 01 21:54:31 EDT 2021 Peter Wu - v6.1.1
- Release v6.1.1
* Sat May 01 09:45:27 EDT 2021 Peter Wu - v6.1.0
- Release v6.1.0
* Sat Apr 24 20:27:51 EDT 2021 Peter Wu - v6.0.1
- Release v6.0.1
* Sat Apr 24 09:54:28 EDT 2021 Peter Wu - v6.0.0
- Release v6.0.0
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
