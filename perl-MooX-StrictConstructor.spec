Name:           perl-MooX-StrictConstructor
Version:        0.008
Release:        1%{?dist}
Summary:        Make your Moo-based object constructors blow up on unknown attributes
License:        GPL+ or Artistic
URL:            http://metacpan.org/release/MooX-StrictConstructor/
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HARTZELL/MooX-StrictConstructor-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Simply loading this module makes your constructors "strict". If your
constructor is called with an attribute init argument that your class does
not declare, then it dies. This is a great way to catch small typos.

%prep
%setup -q -n MooX-StrictConstructor-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*


%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
%exclude %{_libdir}/perl5/vendor_perl/auto/MooX/StrictConstructor/.packlist


%changelog
