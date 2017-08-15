Name:		perl-Cpanel-JSON-XS
Summary:	JSON::XS for Cpanel, fast and correct serializing
Version:	3.0237
Release:        1%{?dist}
License:	GPL+ or Artistic
URL:		http://metacpan.org/release/Cpanel-JSON-XS
Source0:	https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
#BuildRequires:	perl(JSON::PP) >= 2.09
#BuildRequires:	perl(JSON::XS)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Avoid unwanted provides and dependencies
%{?perl_default_filter}

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be correct and its secondary goal is to be fast. To
reach the latter goal it was written in C.

%prep
%setup -q -n Cpanel-JSON-XS-%{version}

# Fix shellbangs
perl -pi -e 's|^#!/opt/bin/perl|#!/usr/bin/perl|' eg/*

# Avoid doc-file dependencies from examples
chmod -c -x eg/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}


%files
%doc COPYING
%doc Changes README eg/
%exclude %{_bindir}/cpanel_json_xs
%{perl_vendorarch}/auto/Cpanel/
%{perl_vendorarch}/Cpanel/
%{_mandir}/man1/cpanel_json_xs.1*
%{_mandir}/man3/Cpanel::JSON::XS.3*
%{_mandir}/man3/Cpanel::JSON::XS::Boolean.3*

%changelog
