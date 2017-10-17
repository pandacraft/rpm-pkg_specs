Name:           libucl
Version:        0.8.0
Release:        1%{?dist}
Summary:        Universal configuration library parser

License:        BSD 2.0
URL:            https://github.com/vstakhov/libucl
Source0:        https://github.com/vstakhov/libucl/archive/%{version}.tar.gz

BuildRequires:  libtool

%description
Universal configuration library parser


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
sh autogen.sh
%configure --disable-static
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING
%{_libdir}/libucl.so{,.*}

%files devel
%_includedir/ucl.h
%_includedir/ucl++.h
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}.3.gz


%changelog
