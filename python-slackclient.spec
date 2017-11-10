%{!?__python27_libdir: %global __python27_libdir %(%{__python27} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python-slackclient
Version:        1.0.9
Release:        1%{?dist}
Summary:        Slack Developer Kit for Python

License:        MIT
URL:            https://pypi.python.org/pypi/slackclient
Source0:        https://github.com/slackapi/%{name}/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python27-devel python27-setuptools
# see requirements in https://github.com/slackapi/python-slackclient/blob/master/setup.py
#Requires:       python(websocket-client) >= 0.35, python(websocket-client) < 1.0a0, python(requests) >= 2.11, python(requests) < 3.0a0, python(six) >= 1.10, python(six) < 2.0a
Requires:       python-websocket-client, python27-six, python27-requests

%description
A basic client for Slack.com, which can optionally connect to the Slack Real Time Messaging (RTM) API.


%prep
%setup -q


%build
%{__python27} setup.py build # --build-lib=/usr/lib/python2.7/dist-packages


%install
rm -rf $RPM_BUILD_ROOT
%{__python27} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python27_libdir}

 
%files
%doc LICENSE README.rst
%{__python27_libdir}/slackclient/*.py
%{__python27_libdir}/*.egg-info
# Do not include python cache files
%exclude %{__python27_libdir}/slackclient/*.pyc
%exclude %{__python27_libdir}/slackclient/*.pyo

%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 1.0.9
- Package creation for production usage on amzn 2017.03
