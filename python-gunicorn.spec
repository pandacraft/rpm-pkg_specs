%define __python_module gunicorn
%define __python_version 36
%define __python_distdir %(%{__python36} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python%{__python_version}-%{__python_module}
Version:        19.7.1
Release:        1%{?dist}
Summary:        WSGI HTTP Server for UNIX

License:        ASL 2.0
URL:            http://gunicorn.org
Source0:        https://github.com/benoitc/gunicorn/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{__python_version}


%description
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.

%prep
%setup -q -n %{__python_module}-%{version}


%build
%{__python36} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python36} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python_distdir}
find $RPM_BUILD_ROOT -depth -type d -name __pycache__ -exec rmdir {} 2>/dev/null ';'

 
%files
%license LICENSE
%doc NOTICE README.rst THANKS
/usr/local/bin/gunicorn
/usr/local/bin/gunicorn_paster
%{__python_distdir}/%{__python_module}
%{__python_distdir}/%{__python_module}-%{version}.egg-info

%changelog
* Fri Nov 10 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 19.7.1
- Package creation for production usage on amzn 2017.09
