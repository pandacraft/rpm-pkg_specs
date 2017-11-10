%define __python_module requests
%define __python_version 27
%define __python_distdir %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python%{__python_version}-%{__python_module}
Version:        2.18.4
Release:        1%{?dist}
Summary:        HTTP library, written in Python, for human beings

License:        ASL 2.0
URL:            http://python-requests.org
Source0:        https://github.com/requests/requests/archive/v%{version}.tar.gz

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
%{__python_distdir}/%{__python_module}-%{version}.egg-info
%exclude %{__python_distdir}/%{__python_module}/*.pyc
%exclude %{__python_distdir}/%{__python_module}/*.pyo

%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 2.18.4
- Package creation for production usage on amzn 2017.03
