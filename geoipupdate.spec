Name:       geoipupdate
Version:    2.4.0
Release:    1%{?dist}
Summary:    Program to perform automatic updates of GeoIP2 and GeoIP databases
Group:      System Environment/Base
License:    GPLv2
URL:        https://github.com/maxmind/geoipupdate
Source0:    https://github.com/maxmind/geoipupdate/releases/download/v%{version}/geoipupdate-%{version}.tar.gz
BuildRequires: curl-devel
BuildRequires: zlib-devel

%description
The GeoIP Update program performs automatic updates of GeoIP2 and
GeoIP Legacy binary databases.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%config(noreplace) /etc/GeoIP.conf
%config /etc/GeoIP.conf.default
%{_bindir}/geoipupdate
%{_mandir}/man1/geoipupdate.1*
%{_mandir}/man5/GeoIP.conf.5*


%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 2.4.0
- Package creation for production usage on amzn 2017.03
