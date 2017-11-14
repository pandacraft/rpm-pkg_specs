%define __python_module flask
%define __python_version 36
%define __python_distdir %(%{__python36} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python-flask
Version:        0.12.2
Release:        1%{?dist}
Summary:        A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions

Group:          Development/Libraries
License:        BSD
URL:            http://flask.pocoo.org/
Source0:        https://github.com/pallets/flask/archive/0.12.2.tar.gz

BuildArch:      noarch
Requires:       python-Werkzeug,python-Jinja2,python-itsdangerous,python-click

%description
Flask is called a “micro-framework” because the idea to keep the core
simple but extensible. There is no database abstraction layer, no form
validation or anything else where different libraries already exist
that can handle that. However Flask knows the concept of extensions
that can add this functionality into your application as if it was
implemented in Flask itself. There are currently extensions for object
relational mappers, form validation, upload handling, various open
authentication technologies and more.

%prep
%setup -q -n %{__python_module}-%{version}


%build
%{__python36} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python36} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python_distdir}
find $RPM_BUILD_ROOT -depth -type d -name __pycache__ -exec rmdir {} 2>/dev/null ';'

%files
%doc AUTHORS LICENSE CHANGES README
%{__python_distdir}/*.egg-info
%{__python_distdir}/flask/*
/usr/local/bin/flask

%changelog
