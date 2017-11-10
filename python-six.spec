%define __python_module six
%{!?__python27_libdir: %global __python27_libdir %(%{__python27} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python27-six
Version:        1.11.0
Release:        1%{?dist}
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
%{__python27} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python27} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python27_libdir}

 
%files
%doc LICENSE README.rst
%{__python27_libdir}/six.py
%{__python27_libdir}/six-%{version}.egg-info
%exclude %{__python27_libdir}/six.pyc
%exclude %{__python27_libdir}/six.pyo

%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 1.11.0
- Package creation for production usage on amzn 2017.03
