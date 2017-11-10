Name:           libmaxminddb
Summary:        C library for the MaxMind DB file format
Version:        1.2.1
Release:        1%{?dist}
URL:            https://maxmind.github.io/libmaxminddb
Source0:        https://github.com/maxmind/libmaxminddb/releases/download/%{version}/%{name}-%{version}.tar.gz
License:        ASL 2.0 and BSD

%description
The package contains libmaxminddb library.

%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Summary:        Development header files for libmaxminddb

%description devel
The package contains development header files for the libmaxminddb library
and the mmdblookup utility which allows IP address lookup in a MaxMind DB file.

%prep
%setup -q

%build
%configure --disable-static
# remove embeded RPATH
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# link only requried libraries
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}

%check
# tests are linked dynamically, preload the library as we have removed RPATH
LD_PRELOAD=%{buildroot}%{_libdir}/libmaxminddb.so make check

%install
%make_install
find "${RPM_BUILD_ROOT}" -type f -name "*.la" -exec rm -fr {} \;

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE
%{_libdir}/libmaxminddb.so
%{_libdir}/libmaxminddb.so.*

%files devel
%doc NOTICE
%doc Changes.md
%{_bindir}/mmdblookup
%{_includedir}/maxminddb.h
%{_includedir}/maxminddb_config.h
%{_libdir}/pkgconfig/libmaxminddb.pc
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 1.2.1
- Package creation for production usage on amzn 2017.03
