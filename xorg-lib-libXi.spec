Summary:	X Input extension library
Summary(pl):	Biblioteka rozszerzenia X Input
Name:		xorg-lib-libXi
Version:	1.1.0
Release:	3
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXi-%{version}.tar.bz2
# Source0-md5:	c25abbe604029855eb11a3a75fb1f386
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-inputproto-devel >= 1.4
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	libXi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Input extension library.

%description -l pl
Biblioteka rozszerzenia X Input.

%package devel
Summary:	Header files for libXi library
Summary(pl):	Pliki nag³ówkowe biblioteki libXi
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-inputproto-devel >= 1.4
Obsoletes:	libXi-devel

%description devel
X Input extension library.

This package contains the header files needed to develop programs that
use libXi.

%description devel -l pl
Biblioteka rozszerzenia X Input.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXi.

%package static
Summary:	Static libXi library
Summary(pl):	Biblioteka statyczna libXi
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXi-static

%description static
X Input extension library.

This package contains the static libXft library.

%description static -l pl
Biblioteka rozszerzenia X Input.

Pakiet zawiera statyczn± bibliotekê libXft.

%prep
%setup -q -n libXi-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXi.so
%{_libdir}/libXi.la
%{_pkgconfigdir}/xi.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXi.a
