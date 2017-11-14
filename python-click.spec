%define __python_module click
%define __python_version 36
%define __python_distdir %(%{__python36} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python-%{__python_module}
Version:        6.7
Release:        1%{?dist}
Summary:        Python composable command line utility

Group:          Development/Libraries
License:        BSD
URL:            http://click.pocoo.org
Source0:        https://pypi.python.org/packages/95/d9/c3336b6b5711c3ab9d1d3a80f1a3e2afeb9d8c02a7166462f6cc96570897/%{__python_module}-%{version}.tar.gz

BuildArch:      noarch


%description
Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary.  It's the "Command
Line Interface Creation Kit".  It's highly configurable but comes with
sensible defaults out of the box.

%prep
%setup -q -n %{__python_module}-%{version}


%build
%{__python36} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python36} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python_distdir}
find $RPM_BUILD_ROOT -depth -type d -name __pycache__ -exec rm -fr {} 2>/dev/null ';'

%files
%license LICENSE
%doc README CHANGES
%{__python_distdir}/*.egg-info
%{__python_distdir}/%{__python_module}/*

%changelog
