Summary:	XSPF playlist reading and writing support
Summary(pl.UTF-8):	Obsługa odczytu i zapisu playlist XSPF
Name:		libspiff
Version:	0.6.5
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/libspiff/%{name}-%{version}.tar.gz
# Source0-md5:	15e3d278e4af956134890108251f72b7
URL:		http://libspiff.sourceforge.net/
BuildRequires:	expat-devel >= 1:1.95.8
BuildRequires:	libstdc++-devel
BuildRequires:	uriparser-devel >= 0.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libSpiff brings XSPF playlist reading and writing support to your C++
application.

%description -l pl.UTF-8
libSpiff daje możliwość odczytu i zapisu playlist XSPF z poziomu C++.

%package devel
Summary:	Header files for libspiff
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libspiff
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	expat-devel >= 1:1.95.8
Requires:	libstdc++-devel
Requires:	uriparser-devel >= 0.3.0

%description devel
Header files for libspiff.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libspiff.

%package static
Summary:	Static libspiff library
Summary(pl.UTF-8):	Statyczna biblioteka libspiff
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libspiff library.

%description static -l pl.UTF-8
Statyczna biblioteka libspiff.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/spiff

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
