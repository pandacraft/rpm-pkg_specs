Name:           mod_maxminddb
Version:        1.1.0
Release:        1%{?dist}
Summary:        MaxMind DB Apache Module

License:        Apache License 2.0
URL:            http:s//maxmind.github.io/mod_maxminddb
Source0:        https://github.com/maxmind/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  httpd24-devel libmaxminddb-devel
Requires:       httpd24 libmaxminddb

%description


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
%make_install 
mkdir -p $RPM_BUILD_ROOT%{_usr}/%{_lib}/httpd/modules
cp %{_usr}/%{_lib}/httpd/modules/%{name}.so $RPM_BUILD_ROOT/usr/%{_lib}/httpd/modules/

%files
%{_usr}/%{_lib}/httpd/modules/%{name}.so


%changelog
