Summary:	X Input extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia X Input
Name:		xorg-lib-libXi
Version:	1.7.1
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXi-%{version}.tar.bz2
# Source0-md5:	24d71afed1b86c60d4eb361628d7f47b
Patch0:		%{name}-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	asciidoc >= 8.4.5
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-lib-libX11-devel >= 1.4.99.901
BuildRequires:	xorg-lib-libXext-devel >= 1:1.0.99.1
# only for typedef
BuildRequires:	xorg-lib-libXfixes-devel >= 5
BuildRequires:	xorg-proto-inputproto-devel >= 2.3
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.3
BuildRequires:	xorg-proto-xproto-devel >= 7.0.13
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
Requires:	xorg-lib-libX11 >= 1.4.99.901
Requires:	xorg-lib-libXext >= 1:1.0.99.1
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
Requires:	xorg-lib-libX11-devel >= 1.4.99.901
Requires:	xorg-lib-libXext-devel >= 1:1.0.99.1
Requires:	xorg-proto-inputproto-devel >= 2.3
Requires:	xorg-proto-xextproto-devel >= 7.0.3
Requires:	xorg-proto-xproto-devel >= 7.0.13
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
%patch0 -p1

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
%doc specs/inputlib.html
%attr(755,root,root) %{_libdir}/libXi.so
%{_libdir}/libXi.la
%{_pkgconfigdir}/xi.pc
%{_includedir}/X11/extensions/XInput*.h
%{_mandir}/man3/X*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXi.a
