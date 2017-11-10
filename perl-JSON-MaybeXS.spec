Name:		perl-JSON-MaybeXS
Summary:	Use Cpanel::JSON::XS with a fallback to JSON::XS and JSON::PP
Version:	1.003009
Release:	1%{?dist}
License:	GPL+ or Artistic
URL:		http://metacpan.org/release/JSON-MaybeXS
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/JSON-MaybeXS-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module first checks to see if either Cpanel::JSON::XS or JSON::XS
is already loaded, in which case it uses that module. Otherwise it tries
to load Cpanel::JSON::XS, then JSON::XS, then JSON::PP in order, and
either uses the first module it finds or throws an error.

It then exports the "encode_json" and "decode_json" functions from the
loaded module, along with a "JSON" constant that returns the class name
for calling "new" on.

If you're writing fresh code rather than replacing JSON.pm usage, you
might want to pass options as constructor args rather than calling
mutators, so we provide our own "new" method that supports that.

%prep
%setup -q -n JSON-MaybeXS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}


%files
%doc Changes README
%{perl_vendorlib}/JSON/
%{_mandir}/man3/JSON::MaybeXS.3*

%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 1.003009
- Package creation for production usage on amzn 2017.03
