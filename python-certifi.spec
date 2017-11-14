%define __python_module certifi
%define __python_version 36
%define __python_distdir %(%{__python36} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python%{__python_version}-%{__python_module}
Version:        2017.11.05
Release:        1%{?dist}
Summary:        Mozilla's SSL Certs

License:        MPL 2.0
URL:            https://pypi.python.org/pypi/certifi
Source0:        https://github.com/certifi/python-certifi/archive/2017.11.05.tar.gz

BuildArch:      noarch
BuildRequires:  python%{__python_version}


%description
This package provides the path to Mozilla's CA bundle for SSL.

%prep
%setup -q -n python-%{__python_module}-%{version}


%build
%{__python36} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python36} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python_distdir}

%files
%doc README.rst LICENSE
%{__python_distdir}*

%changelog
* Fri Nov 10 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 19.7.1
- Package creation for production usage on amzn 2017.09
