%define __python_module itsdangerous
%define __python_version 36
%define __python_distdir %(%{__python36} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python-%{__python_module}
Version:        0.24
Release:        1%{?dist}
Summary:        Various helpers to pass trusted data to untrusted environments

License:        BSD 3.0
URL:            https://pythonhosted.org/itsdangerous
Source0:        https://pypi.python.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/%{__python_module}-%{version}.tar.gz

BuildArch:      noarch

%description

It’s Dangerous
    … so better sign this

Various helpers to pass data to untrusted environments and to get it back safe and sound.

This repository provides a module that is a port of the django signing module. It’s not directly copied but some changes were applied to make it work better on its own.

%prep
%setup -q -n %{__python_module}-%{version}


%build
%{__python36} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python36} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python_distdir}
find $RPM_BUILD_ROOT -depth -type d -name __pycache__ -exec rm  -fr {} 2>/dev/null ';'

 
%files
%doc README CHANGES
%license LICENSE
%{__python_distdir}/%{__python_module}*.py
%{__python_distdir}/%{__python_module}-%{version}.egg-info

%changelog
