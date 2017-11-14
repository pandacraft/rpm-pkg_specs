%define __python_module MarkupSafe
%define __python_version 36
%define __python_distdir %(%{__python36} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python-%{__python_module}
Version:        1.0
Release:        1%{?dist}
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python

Group:          Development/Libraries
License:        BSD
URL:            http://www.pocoo.org/projects/markupsafe
Source0:        https://pypi.python.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/%{__python_module}-%{version}.tar.gz

BuildArch:      %{_arch}

%description
Implements a unicode subclass that supports HTML strings

%prep
%setup -q -n %{__python_module}-%{version}


%build
%{__python36} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python36} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python_distdir}
find $RPM_BUILD_ROOT -depth -type d -name __pycache__ -exec rmdir {} 2>/dev/null ';'

%files
%doc AUTHORS LICENSE README.rst
%{__python_distdir}/*

%changelog
