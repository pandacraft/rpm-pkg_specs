%define __python_module six
%define __python_distdir %(%{__python36} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python36-six
Version:        1.11.0
Release:        2%{?dist}
Summary:        Python 2 and 3 compatibility library

License:        MIT
URL:            http://six.readthedocs.io
Source0:        https://github.com/benjaminp/six/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python27-devel python27-setuptools

%description
Six is a Python 2 and 3 compatibility library. It provides utility functions for smoothing over the differences between the Python versions with the goal of writing Python code that is compatible on both Python versions. See the documentation for more information on what is provided.


%prep
%setup -q -n %{__python_module}-%{version}


%build
%{__python36} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python36} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python_distdir}

 
%files
%doc LICENSE README.rst
%{__python_distdir}/six.py
%{__python_distdir}/six-%{version}.egg-info
%exclude %{__python_distdir}/__pycache__

%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 1.11.0
- Package creation for production usage on amzn 2017.03
