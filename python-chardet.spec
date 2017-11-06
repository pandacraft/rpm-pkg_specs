%define __python_module chardet
%define __python_version 27
%define __python_distdir %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python%{__python_version}-%{__python_module}
Version:        3.0.4
Release:        1%{?dist}
Summary:        Universal encoding detector for Python 2 and 3

License:        LGPL
URL:            https://chardet.readthedocs.io
Source0:        https://github.com/chardet/chardet/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{__python_version}-setuptools

%description
Requests allows you to send organic, grass-fed HTTP/1.1 requests, without the need for manual labor. There's no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, thanks to urllib3.

%prep
%setup -q -n %{__python_module}-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python_distdir}

 
%files
%doc LICENSE README.rst
%{__python_distdir}/%{__python_module}/*.py
%{__python_distdir}/%{__python_module}/cli/*.py
%{__python_distdir}/%{__python_module}-%{version}.egg-info
/usr/local/bin/chardetect
%exclude %{__python_distdir}/%{__python_module}/*.pyc
%exclude %{__python_distdir}/%{__python_module}/cli/*.pyc
%exclude %{__python_distdir}/%{__python_module}/*.pyo
%exclude %{__python_distdir}/%{__python_module}/cli/*.pyo

%changelog
