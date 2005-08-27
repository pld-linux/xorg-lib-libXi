Summary:	X Input extension library
Summary(pl):	Biblioteka rozszerzenia X Input
Name:		xorg-lib-libXi
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXi-%{version}.tar.bz2
# Source0-md5:	d5ac64bc61c1b80cae30a4cc789d4af4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
X Input extension library.

%description -l pl
Biblioteka rozszerzenia X Input.

%package devel
Summary:	Header files libXi development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXi
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Obsoletes:	libXi-devel

%description devel
X Input extension library.

This package contains the header files needed to develop programs that
use these libXi.

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
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libXi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXi.so
%{_libdir}/libXi.la
%{_pkgconfigdir}/xi.pc
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXi.a
