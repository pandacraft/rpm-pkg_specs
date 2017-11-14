%define __python_libdir %(%{_libexecdir}/system-python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python-libui
Version:        0.0.1
Release:        1%{?dist}
Summary:        Python 3 wrapper for the libui library

License:        MIT
URL:            https://github.com/waghanza/pylibui
Source0:        https://github.com/waghanza/pylibui/archive/fix_setup.tar.gz

BuildArch:      noarch

Requires:       libui

%description
Python 3 wrapper for libui. It uses cffi to interface with the libui shared library.

Almost auto binding generation with few exceptions

%prep
%setup -q -n pylibui-fix_setup


%build
%{_libexecdir}/system-python setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{_libexecdir}/system-python setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python_libdir}

 
%files
%doc README.md LICENSE
%{__python_libdir}/pylibui/*.py
%{__python_libdir}/pylibui/libui/*.py
%{__python_libdir}/pylibui/controls/*.py
%{__python_libdir}/*.egg-info
%exclude %{__python_libdir}/pylibui/__pycache__/*
%exclude %{__python_libdir}/pylibui/libui/__pycache__/*
%exclude %{__python_libdir}/pylibui/controls/__pycache__/*


%changelog
