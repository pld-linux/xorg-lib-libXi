Summary:	X Input extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia X Input
Name:		xorg-lib-libXi
Version:	1.8
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXi-%{version}.tar.bz2
# Source0-md5:	74055672a111a98ce2841d2ec4057b05
Patch0:		%{name}-man.patch
URL:		https://xorg.freedesktop.org/
BuildRequires:	asciidoc >= 8.4.5
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-lib-libXext-devel >= 1:1.0.99.1
# only for typedef
BuildRequires:	xorg-lib-libXfixes-devel >= 5
BuildRequires:	xorg-proto-inputproto-devel >= 2.3.99.1
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.3
BuildRequires:	xorg-proto-xproto-devel >= 7.0.13
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
Requires:	xorg-lib-libX11 >= 1.6
Requires:	xorg-lib-libXext >= 1:1.0.99.1
Obsoletes:	libXi < 6.0.2
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
Requires:	xorg-lib-libX11-devel >= 1.6
Requires:	xorg-lib-libXext-devel >= 1:1.0.99.1
Requires:	xorg-proto-inputproto-devel >= 2.3.99.1
Requires:	xorg-proto-xextproto-devel >= 7.0.3
Requires:	xorg-proto-xproto-devel >= 7.0.13
Obsoletes:	libXi-devel < 6.0.2

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
Obsoletes:	libXi-static < 6.0.2

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
%configure \
	--without-fop
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

# (HTML version) packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/libXi/inputlib.*
# XML source
%{__rm} $RPM_BUILD_ROOT%{_docdir}/libXi/*.xml

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXi.so.6

%files devel
%defattr(644,root,root,755)
%doc specs/inputlib.html
%attr(755,root,root) %{_libdir}/libXi.so
%{_libdir}/libXi.la
%{_pkgconfigdir}/xi.pc
%{_includedir}/X11/extensions/XInput*.h
%{_mandir}/man3/X*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXi.a
