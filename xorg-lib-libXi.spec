Summary:	X Input extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia X Input
Name:		xorg-lib-libXi
Version:	1.3
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXi-%{version}.tar.bz2
# Source0-md5:	8df4ece9bd1efb02c28acb2b6f485e09
URL:		http://xorg.freedesktop.org/
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xmlto
BuildRequires:	xorg-lib-libX11-devel >= 1.2.99.1
BuildRequires:	xorg-lib-libXext-devel >= 1:1.0.99.1
BuildRequires:	xorg-proto-inputproto-devel >= 1.9.99.902
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.3
BuildRequires:	xorg-proto-xproto-devel >= 7.0.13
BuildRequires:	xorg-util-util-macros >= 1.3
Obsoletes:	libXi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Input extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia X Input.

%package devel
Summary:	Header files for libXi library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXi
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel >= 1:1.0.99.1
Requires:	xorg-proto-inputproto-devel >= 1.9.99.902
Obsoletes:	libXi-devel

%description devel
X Input extension library.

This package contains the header files needed to develop programs that
use libXi.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia X Input.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXi.

%package static
Summary:	Static libXi library
Summary(pl.UTF-8):	Biblioteka statyczna libXi
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXi-static

%description static
X Input extension library.

This package contains the static libXft library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia X Input.

Pakiet zawiera statyczną bibliotekę libXft.

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXi.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXi.so
%{_libdir}/libXi.la
%{_pkgconfigdir}/xi.pc
%{_includedir}/X11/extensions/XInput*.h
%{_mandir}/man3/X*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXi.a
