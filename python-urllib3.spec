%define __python_module urllib3
%define __python_version 36
%define __python_distdir %(%{__python36} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python%{__python_version}-urllib3
Version:        1.22
Release:        2%{?dist}
Summary:        Python HTTP library with thread-safe connection pooling, file post support, sanity friendly, and more.

License:        MIT
URL:            http://urllib3.readthedocs.org
Source0:        https://github.com/shazow/urllib3/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{__python_version}-setuptools

%description
urllib3 is a powerful, sanity-friendly HTTP client for Python. Much of the Python ecosystem already uses urllib3 and you should too. urllib3 brings many critical features that are missing from the Python standard libraries:
* Thread safety.
* Connection pooling.
* Client-side SSL/TLS verification.
* File uploads with multipart encoding.
* Helpers for retrying requests and dealing with HTTP redirects.
* Support for gzip and deflate encoding.
* Proxy support for HTTP and SOCKS.
* 100% test coverage.

%prep
%setup -q -n %{__python_module}-%{version}


%build
%{__python36} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python36} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python_distdir}

 
%files
%doc CHANGES.rst LICENSE.txt README.rst CONTRIBUTORS.txt
%{__python_distdir}/*

%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 1.22
- Package creation for production usage on amzn 2017.03
