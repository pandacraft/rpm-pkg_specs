Name:           mydumper
Version:        0.9.3
Release:        1%{?dist}
Summary:        How MySQL DBA & support engineer would imagine 'mysqldump' ;-)

License:        GNU GPL v3
URL:            https://github.com/maxbube/mydumper
Source0:        https://github.com/maxbube/mydumper/archive/v%{version}.tar.gz

BuildRequires:  gcc gcc-c++ cmake glib2-devel mysql57-devel zlib-devel pcre-devel openssl-devel
Requires:       mysql57-devel

%description
* Parallelism (hence, speed) and performance (avoids expensive character set conversion routines, efficient code overall)
* Easier to manage output (separate files for tables, dump metadata, etc, easy to view/parse data)
* Consistency - maintains snapshot across all threads, provides accurate master and slave log positions, etc
* Manageability - supports PCRE for specifying database and tables inclusions and exclusions

%prep
%setup -q


%build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_bindir}/mydumper
%{_bindir}/myloader
%doc


%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 0.9.3
- Package creation for production usage on amzn 2017.03
