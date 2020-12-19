%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-curly-slab
Version:        4.1.1
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

# Iosevka Curly Slab — Monospace, Curly Style, Slab-serif
%package -n iosevka-curly-slab-fonts
Summary:        Monospace, Curly Style, Slab-serif
%description -n iosevka-curly-slab-fonts
Iosevka Monospace, Curly Style, Slab-serif

%package -n iosevka-term-curly-slab-fonts
Summary:        Monospace, Curly Style, Slab-serif
%description -n iosevka-term-curly-slab-fonts
Iosevka Monospace, Curly Style, Slab-serif

%package -n iosevka-fixed-curly-slab-fonts
Summary:        Monospace, Curly Style, Slab-serif
%description -n iosevka-fixed-curly-slab-fonts
Iosevka Monospace, Curly Style, Slab-serif

%build
npm install

npm run build -- ttf::iosevka-curly-slab
npm run build -- ttf::iosevka-term-curly-slab
npm run build -- ttf::iosevka-fixed-curly-slab

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-curly-slab/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-curly-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-curly-slab/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-curly-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-curly-slab/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-curly-slab-fonts

# Iosevka Curly Slab — Monospace, Curly Style, Slab-serif
%files -n iosevka-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-curly-slab-fonts/*

%files -n iosevka-term-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-curly-slab-fonts/*

%files -n iosevka-fixed-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-curly-slab-fonts/*

%changelog
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
