%define		_state		stable
%define		orgname		ksquares
%define		qtver		4.8.0

Summary:	Ksquares
Name:		kde4-%{orgname}
Version:	4.14.3
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	a6471674384cc934a36e59424f14064f
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ksquares.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksquares
%{_desktopdir}/kde4/ksquares.desktop
%{_datadir}/config.kcfg/ksquares.kcfg
%{_datadir}/apps/ksquares
%{_iconsdir}/*/*/apps/ksquares.png
