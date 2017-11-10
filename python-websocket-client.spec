# Ignore unpackaged file warning
%define _unpackaged_files_terminate_build 0

# Define pythoon module name
%define __python_module websocket-client

# Define install path
%{!?__python27_libdir: %global __python27_libdir %(%{__python27} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-websocket-client
Version:        0.43.0
Release:        1%{?dist}
Summary:        websocket client for python

License:        MIT
URL:            https://pypi.python.org/pypi/websocket-client
Source0:        https://github.com/websocket-client/websocket-client/archive/v0.43.0.tar.gz

BuildArch:      noarch
BuildRequires:  python27-devel python27-setuptools

%description
websocket-client module is WebSocket client for python. This provide the low level APIs for WebSocket. All APIs are the synchronous functions.


%prep
%setup -q -n %{__python_module}-%{version}


%build
%{__python27} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python27} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python27_libdir}

 
%files
%doc LICENSE README.rst
%{__python27_libdir}/websocket/*.py
%{__python27_libdir}/websocket_client-%{version}.egg-info
%exclude %{__python27_libdir}/websocket/*.pyc
%exclude %{__python27_libdir}/websocket/*.pyo
%exclude %{__python27_libdir}/websocket/tests
%exclude %{__python27_libdir}/websocket/cacert.pem

%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 0.43.0
- Package creation for production usage on amzn 2017.03
