#
# Conditional build
%bcond_without	static_libs	# don't build static library
%bcond_without  tests		# disable cpptest
#
Summary:	XSPF playlist reading and writing support
Summary(pl.UTF-8):	Obsługa odczytu i zapisu playlist XSPF
Name:		libxspf
Version:	1.2.0
Release:	5
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libspiff/%{name}-%{version}.tar.gz
# Source0-md5:	d3276bf6c7f86442b72629a3e7b8bd5b
Patch0:		%{name}-link.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-gcc47.patch
URL:		http://libspiff.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_tests:BuildRequires:	cpptest-devel >= 1.1.0}
BuildRequires:	expat-devel >= 1:1.95.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	uriparser-devel >= 0.7.5
Requires:	expat >= 1:1.95.8
Requires:	uriparser >= 0.7.5
Obsoletes:	libspiff
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxspf brings XSPF playlist reading and writing support to your C++
application.

%description -l pl.UTF-8
libxspf daje możliwość odczytu i zapisu playlist XSPF z poziomu C++.

%package devel
Summary:	Header files for libxspf
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxspf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	expat-devel >= 1:1.95.8
Requires:	libstdc++-devel
Requires:	uriparser-devel >= 0.3.0
Obsoletes:	libspiff-devel

%description devel
Header files for libxspf.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxspf.

%package static
Summary:	Static libxspf library
Summary(pl.UTF-8):	Statyczna biblioteka libxspf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libspiff-static

%description static
Static libxspf library.

%description static -l pl.UTF-8
Statyczna biblioteka libxspf.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	 %{!?with_tests:--disable-test}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxspf.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/xspf_*
%attr(755,root,root) %{_libdir}/libxspf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxspf.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxspf.so
%{_includedir}/xspf
%{_pkgconfigdir}/xspf.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxspf.a
%endif
