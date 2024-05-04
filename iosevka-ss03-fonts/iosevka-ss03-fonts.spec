%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss03
Version:        30.0.0
Release:        1%{?dist}
Summary:        Slender typeface for code, from code.

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  nodejs-npm
BuildRequires:  ttfautohint

%description
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.

%prep
%autosetup -n %{source_name}-%{version}

# Iosevka SS03 — Monospace, Consolas Style
%package -n iosevka-ss03-fonts
Summary:        Monospace, Consolas Style
%description -n iosevka-ss03-fonts
Iosevka Monospace, Consolas Style

%package -n iosevka-term-ss03-fonts
Summary:        Monospace, Consolas Style
%description -n iosevka-term-ss03-fonts
Iosevka Monospace, Consolas Style

%package -n iosevka-fixed-ss03-fonts
Summary:        Monospace, Consolas Style
%description -n iosevka-fixed-ss03-fonts
Iosevka Monospace, Consolas Style

%build
npm install

npm run build -- ttf::IosevkaSS03
npm run build -- ttf::IosevkaTermSS03
npm run build -- ttf::IosevkaFixedSS03

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/IosevkaSS03/TTF/*.ttf      -t %{buildroot}%{_datadir}/fonts/iosevka-ss03-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/IosevkaTermSS03/TTF/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss03-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/IosevkaFixedSS03/TTF/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss03-fonts

# Iosevka SS03 — Monospace, Consolas Style
%files -n iosevka-ss03-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss03-fonts/*

%files -n iosevka-term-ss03-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss03-fonts/*

%files -n iosevka-fixed-ss03-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss03-fonts/*

%changelog
* Sat May 04 11:02:05 EDT 2024 Peter Wu - v30.0.0
- Release v30.0.0
* Sat Apr 20 09:48:25 EDT 2024 Peter Wu - v29.2.1
- Release v29.2.1
* Sat Apr 13 13:14:05 EDT 2024 Peter Wu - v29.2.0
- Release v29.2.0
* Sat Apr 06 09:47:29 EDT 2024 Peter Wu - v29.1.0
- Release v29.1.0
* Sat Mar 30 15:16:29 EDT 2024 Peter Wu - v29.0.5
- Release v29.0.5
* Mon Mar 25 15:01:36 EDT 2024 Peter Wu - v29.0.4
- Release v29.0.4
* Sun Mar 24 09:54:27 EDT 2024 Peter Wu - v29.0.3
- Release v29.0.3
* Sat Mar 23 18:04:39 EDT 2024 Peter Wu - v29.0.2
- Release v29.0.2
* Sun Mar 10 14:28:43 EDT 2024 Peter Wu - v29.0.1
- Release v29.0.1
* Sat Mar 09 10:08:29 EST 2024 Peter Wu - v29.0.0
- Release v29.0.0
* Sun Feb 04 09:58:38 EST 2024 Peter Wu - v28.1.0
- Release v28.1.0
* Sat Jan 27 08:28:25 EST 2024 Peter Wu - v28.0.7
- Release v28.0.7
* Sat Jan 20 20:21:27 EST 2024 Peter Wu - v28.0.6
- Release v28.0.6
* Sat Jan 13 10:24:05 EST 2024 Peter Wu - v28.0.5
- Release v28.0.5
* Sat Jan 06 08:49:45 EST 2024 Peter Wu - v28.0.4
- Release v28.0.4
* Sat Dec 30 10:09:52 EST 2023 Peter Wu - v28.0.3
- Release v28.0.3
* Sat Dec 23 14:56:31 EST 2023 Peter Wu - v28.0.2
- Release v28.0.2
* Sun Dec 17 19:24:10 EST 2023 Peter Wu - v28.0.1
- Release v28.0.1
* Sat Dec 16 10:14:58 EST 2023 Peter Wu - v28.0.0
- Release v28.0.0
* Sat Nov 11 11:20:01 EST 2023 Peter Wu - v27.3.5
- Release v27.3.5
* Sat Nov 04 10:10:20 EDT 2023 Peter Wu - v27.3.4
- Release v27.3.4
* Sun Oct 29 08:58:14 EDT 2023 Peter Wu - v27.3.3
- Release v27.3.3
* Sat Oct 28 18:59:08 EDT 2023 Peter Wu - v27.3.2
- Release v27.3.2
* Sun Oct 22 19:39:49 EDT 2023 Peter Wu - v27.3.1
- Release v27.3.1
* Sat Oct 21 10:55:36 EDT 2023 Peter Wu - v27.3.0
- Release v27.3.0
* Sat Oct 14 11:46:54 EDT 2023 Peter Wu - v27.2.1
- Release v27.2.1
* Sat Oct 07 14:01:55 EDT 2023 Peter Wu - v27.2.0
- Release v27.2.0
* Sat Sep 30 13:04:40 EDT 2023 Peter Wu - v27.1.0
- Release v27.1.0
* Sat Sep 23 10:58:32 EDT 2023 Peter Wu - v27.0.2
- Release v27.0.2
* Sun Sep 17 10:29:33 EDT 2023 Peter Wu - v27.0.1
- Release v27.0.1
* Sat Sep 16 10:07:47 EDT 2023 Peter Wu - v27.0.0
- Release v27.0.0
* Sat Sep 09 10:09:34 EDT 2023 Peter Wu - v26.3.3
- Release v26.3.3
* Mon Sep 04 09:10:38 EDT 2023 Peter Wu - v26.3.2
- Release v26.3.2
* Sun Sep 03 22:31:55 EDT 2023 Peter Wu - v26.3.1
- Release v26.3.1
* Sat Sep 02 09:50:49 EDT 2023 Peter Wu - v26.3.0
- Release v26.3.0
* Sat Aug 26 08:54:36 EDT 2023 Peter Wu - v26.2.2
- Release v26.2.2
* Sun Aug 20 11:29:08 EDT 2023 Peter Wu - v26.2.1
- Release v26.2.1
* Sat Aug 19 09:26:09 EDT 2023 Peter Wu - v26.2.0
- Release v26.2.0
* Sat Aug 12 22:06:06 EDT 2023 Peter Wu - v26.1.0
- Release v26.1.0
* Sun Aug 06 11:11:21 EDT 2023 Peter Wu - v26.0.2
- Release v26.0.2
* Sat Aug 05 10:19:43 EDT 2023 Peter Wu - v26.0.1
- Release v26.0.1
* Sat Aug 05 00:28:41 EDT 2023 Peter Wu - v26.0.0
- Release v26.0.0
* Sun Jul 23 09:53:32 EDT 2023 Peter Wu - v25.1.1
- Release v25.1.1
* Sat Jul 22 10:29:00 EDT 2023 Peter Wu - v25.1.0
- Release v25.1.0
* Sun Jul 09 13:52:59 EDT 2023 Peter Wu - v25.0.1
- Release v25.0.1
* Sat Jul 08 12:15:34 EDT 2023 Peter Wu - v25.0.0
- Release v25.0.0
* Sat Jun 24 09:51:11 EDT 2023 Peter Wu - v24.1.4
- Release v24.1.4
* Mon Jun 12 08:47:09 EDT 2023 Peter Wu - v24.1.3
- Release v24.1.3
* Sat Jun 10 22:02:09 EDT 2023 Peter Wu - v24.1.2
- Release v24.1.2
* Sat Jun 03 10:52:37 EDT 2023 Peter Wu - v24.1.1
- Release v24.1.1
* Sun May 28 20:14:08 EDT 2023 Peter Wu - v24.1.0
- Release v24.1.0
* Sun May 28 20:13:56 EDT 2023 Peter Wu - v24.0.0
- Release v24.0.0
* Sun May 21 08:44:02 EDT 2023 Peter Wu - v23.0.0
- Release v23.0.0
* Sat May 13 07:57:11 EDT 2023 Peter Wu - v22.1.2
- Release v22.1.2
* Sat May 06 10:29:08 EDT 2023 Peter Wu - v22.1.1
- Release v22.1.1
* Sun Apr 23 12:14:00 EDT 2023 Peter Wu - v22.1.0
- Release v22.1.0
* Sat Apr 15 10:03:04 EDT 2023 Peter Wu - v22.0.2
- Release v22.0.2
* Sat Apr 08 09:37:45 EDT 2023 Peter Wu - v22.0.1
- Release v22.0.1
* Sat Apr 01 09:43:21 EDT 2023 Peter Wu - v22.0.0
- Release v22.0.0
* Sun Mar 26 22:01:38 EDT 2023 Peter Wu - v21.1.1
- Release v21.1.1
* Sat Mar 11 08:36:24 EST 2023 Peter Wu - v21.0.0
- Release v21.0.0
* Sat Mar 04 11:42:30 EST 2023 Peter Wu - v20.0.0
- Release v20.0.0
* Sat Feb 18 17:19:02 EST 2023 Peter Wu - v19.0.1
- Release v19.0.1
* Sun Feb 12 13:05:26 EST 2023 Peter Wu - v19.0.0
- Release v19.0.0
* Fri Feb 03 22:43:47 EST 2023 Peter Wu - v18.0.0
- Release v18.0.0
* Sun Jan 22 09:45:04 EST 2023 Peter Wu - v17.1.0
- Release v17.1.0
* Sat Jan 14 15:58:20 EST 2023 Peter Wu - v17.0.4
- Release v17.0.4
* Sat Jan 14 08:22:03 EST 2023 Peter Wu - v17.0.3
- Release v17.0.3
* Tue Dec 27 13:24:32 EST 2022 Peter Wu - v17.0.2
- Release v17.0.2
* Sat Dec 24 09:58:31 EST 2022 Peter Wu - v17.0.1
- Release v17.0.1
* Fri Dec 23 12:11:03 EST 2022 Peter Wu - v17.0.0
- Release v17.0.0
* Tue Dec 20 09:11:52 EST 2022 Peter Wu - v16.8.4
- Release v16.8.4
* Mon Dec 19 08:51:47 EST 2022 Peter Wu - v16.8.3
- Release v16.8.3
* Sun Dec 18 09:30:28 EST 2022 Peter Wu - v16.8.2
- Release v16.8.2
* Sat Dec 17 16:04:41 EST 2022 Peter Wu - v16.8.1
- Release v16.8.1
* Fri Dec 16 21:51:07 EST 2022 Peter Wu - v16.8.0
- Release v16.8.0
* Mon Dec 12 12:03:34 EST 2022 Peter Wu - v16.7.0
- Release v16.7.0
* Sat Dec 03 19:46:20 EST 2022 Peter Wu - v16.6.0
- Release v16.6.0
* Sat Nov 26 11:39:00 EST 2022 Peter Wu - v16.5.0
- Release v16.5.0
* Sun Nov 20 13:19:40 EST 2022 Peter Wu - v16.4.0
- Release v16.4.0
* Tue Nov 01 19:00:26 EDT 2022 Peter Wu - v16.3.6
- Release v16.3.6
* Sat Oct 15 11:03:51 EDT 2022 Peter Wu - v16.3.4
- Release v16.3.4
* Mon Oct 10 09:55:43 EDT 2022 Peter Wu - v16.3.3
- Release v16.3.3
* Sun Oct 09 10:13:43 EDT 2022 Peter Wu - v16.3.2
- Release v16.3.2
* Sat Oct 08 19:36:46 EDT 2022 Peter Wu - v16.3.1
- Release v16.3.1
* Sun Oct 02 10:57:41 EDT 2022 Peter Wu - v16.3.0
- Release v16.3.0
* Sat Oct 01 08:50:03 EDT 2022 Peter Wu - v16.2.1
- Release v16.2.1
* Sat Sep 10 12:32:32 EDT 2022 Peter Wu - v16.2.0
- Release v16.2.0
* Sun Sep 04 13:42:29 EDT 2022 Peter Wu - v16.1.0
- Release v16.1.0
* Sun Aug 28 10:35:07 EDT 2022 Peter Wu - v16.0.2
- Release v16.0.2
* Sat Aug 27 07:13:37 EDT 2022 Peter Wu - v16.0.1
- Release v16.0.1
* Sat Aug 20 09:42:48 EDT 2022 Peter Wu - v16.0.0
- Release v16.0.0
* Sat Aug 06 09:53:52 EDT 2022 Peter Wu - v15.6.3
- Release v15.6.3
* Sat Jul 30 10:34:11 EDT 2022 Peter Wu - v15.6.2
- Release v15.6.2
* Sat Jul 23 08:59:29 EDT 2022 Peter Wu - v15.6.1
- Release v15.6.1
* Sat Jul 16 10:59:46 EDT 2022 Peter Wu - v15.6.0
- Release v15.6.0
* Sat Jun 25 10:38:40 EDT 2022 Peter Wu - v15.5.2
- Release v15.5.2
* Sat Jun 18 16:34:58 EDT 2022 Peter Wu - v15.5.1
- Release v15.5.1
* Sat Jun 04 09:31:33 EDT 2022 Peter Wu - v15.5.0
- Release v15.5.0
* Mon May 30 20:18:30 EDT 2022 Peter Wu - v15.4.2
- Release v15.4.2
* Sun May 29 08:37:08 EDT 2022 Peter Wu - v15.4.1
- Release v15.4.1
* Sat May 28 20:18:14 EDT 2022 Peter Wu - v15.4.0
- Release v15.4.0
* Sat May 14 09:43:38 EDT 2022 Peter Wu - v15.3.1
- Release v15.3.1
* Sun May 08 09:21:36 EDT 2022 Peter Wu - v15.3.0
- Release v15.3.0
* Sat Apr 16 08:12:09 EDT 2022 Peter Wu - v15.2.0
- Release v15.2.0
* Sat Mar 26 09:57:44 EDT 2022 Peter Wu - v15.1.0
- Release v15.1.0
* Sat Mar 19 12:02:55 EDT 2022 Peter Wu - v15.0.3
- Release v15.0.3
* Mon Mar 07 15:57:08 EST 2022 Peter Wu - v15.0.2
- Release v15.0.2
* Sun Feb 27 09:15:25 EST 2022 Peter Wu - v15.0.1
- Release v15.0.1
* Sat Feb 26 08:47:35 EST 2022 Peter Wu - v15.0.0
- Release v15.0.0
* Sat Feb 19 10:06:58 EST 2022 Peter Wu - v14.0.1
- Release v14.0.1
* Sun Feb 13 10:54:10 EST 2022 Peter Wu - v14.0.0
- Release v14.0.0
* Sat Feb 12 14:42:52 EST 2022 Peter Wu - v13.3.1
- Release v13.3.1
* Sat Feb 12 10:32:23 EST 2022 Peter Wu - v11.3.1
- Release v11.3.1
* Sat Feb 05 22:11:32 EST 2022 Peter Wu - v11.3.0
- Release v11.3.0
* Sun Jan 23 20:30:03 EST 2022 Peter Wu - v11.2.7
- Release v11.2.7
* Sun Jan 09 09:57:44 EST 2022 Peter Wu - v11.2.6
- Release v11.2.6
* Sat Jan 08 09:39:15 EST 2022 Peter Wu - v11.2.5
- Release v11.2.5
* Tue Dec 28 13:45:38 EST 2021 Peter Wu - v11.2.4
- Release v11.2.4
* Mon Dec 27 21:59:35 EST 2021 Peter Wu - v11.2.3
- Release v11.2.3
* Sun Dec 19 15:38:51 EST 2021 Peter Wu - v11.2.2
- Release v11.2.2
* Sat Dec 11 21:50:10 EST 2021 Peter Wu - v11.2.1
- Release v11.2.1
* Sat Dec 04 09:56:08 EST 2021 Peter Wu - v11.2.0
- Release v11.2.0
* Sun Nov 28 09:06:04 EST 2021 Peter Wu - v11.1.1
- Release v11.1.1
* Sun Nov 21 10:49:55 EST 2021 Peter Wu - v11.1.0
- Release v11.1.0
* Sun Nov 07 22:13:49 EST 2021 Peter Wu - v11.0.1
- Release v11.0.1
* Sat Nov 06 21:29:08 EDT 2021 Peter Wu - v11.0.0
- Release v11.0.0
* Sun Oct 24 09:50:11 EDT 2021 Peter Wu - v10.3.4
- Release v10.3.4
* Sun Oct 17 17:40:04 EDT 2021 Peter Wu - v10.3.3
- Release v10.3.3
* Sun Oct 10 10:02:12 EDT 2021 Peter Wu - v10.3.2
- Release v10.3.2
* Sat Oct 02 16:53:07 EDT 2021 Peter Wu - v10.3.1
- Release v10.3.1
* Sun Sep 19 09:16:40 EDT 2021 Peter Wu - v10.3.0
- Release v10.3.0
* Sat Sep 11 17:14:07 EDT 2021 Peter Wu - v10.2.0
- Release v10.2.0
* Sat Aug 28 17:42:30 EDT 2021 Peter Wu - v10.1.1
- Release v10.1.1
* Sat Aug 21 09:36:06 EDT 2021 Peter Wu - v10.1.0
- Release v10.1.0
* Sat Aug 14 09:39:14 EDT 2021 Peter Wu - v10.0.0
- Release v10.0.0
* Sun Aug 01 08:54:31 EDT 2021 Peter Wu - v9.0.1
- Release v9.0.1
* Sat Jul 31 14:23:12 EDT 2021 Peter Wu - v9.0.0
- Release v9.0.0
* Tue Jul 27 11:06:57 EDT 2021 Peter Wu - v8.0.2
- Release v8.0.2
* Mon Jul 26 12:07:04 EDT 2021 Peter Wu - v8.0.1
- Release v8.0.1
* Sun Jul 25 08:08:08 EDT 2021 Peter Wu - v8.0.0
- Release v8.0.0
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
