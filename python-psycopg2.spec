%define __python_module psycopg2
%define __python_version 36
%define __python_distdir %(%{__python36} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python-psycopg2
Version:        2.7.3.2
Release:        1%{?dist}
Summary:        A PostgreSQL database adapter for Python

Group:          Applications/Databases
License:        LGPLv3+ with exceptions
URL:            http://initd.org/psycopg
Source0:        https://pypi.python.org/packages/dd/47/000b405d73ca22980684fd7bd3318690cc03cfa3b2ae1c5b7fff8050b28a/%{__python_module}-%{version}.tar.gz

BuildRequires:  postgresql96-devel
Requires:  postgresql96-libs

%description
Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection). It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent "INSERT"s or "UPDATE"s.

%prep
%setup -q -n %{__python_module}-%{version}


%build
%{__python36} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python36} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python_distdir}
find $RPM_BUILD_ROOT -depth -type d -name __pycache__ -exec rmdir {} 2>/dev/null ';'

%files
%doc AUTHORS NEWS README.rst
%license LICENSE
%{__python_distdir}/*.egg-info
%{__python_distdir}/%{__python_module}/*

%changelog
