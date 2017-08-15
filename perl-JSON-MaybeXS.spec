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
* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.003009-2
- Perl 5.26 rebuild

* Mon Feb 27 2017 Paul Howarth <paul@city-fan.org> - 1.003009-1
- Update to 1.003009
  - Fix tests to no longer rely on . being in @INC (CPAN RT#120404)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.003008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct  3 2016 Paul Howarth <paul@city-fan.org> - 1.003008-1
- Update to 1.003008
  - Added an INSTALLATION section to documentation, to clarify the use of
    dynamic prerequisites in Makefile.PL
  - Minimize prereqs listed in META.json to avoid giving the appearance of XS
    prerequisites, and confusing static inspection tools such as metacpan.org

* Mon Sep 12 2016 Paul Howarth <paul@city-fan.org> - 1.003007-1
- Update to 1.003007
  - Bump prereq on JSON::PP, to ensure we get the fix for parsing utf8-encoded
    values
  - We now always upgrade JSON::XS if it is installed and below version 3.0,
    due to changes in handling booleans
  - Remove test dependency on Test::Without::Module (CPAN RT#115394)
- Simplify find command using -delete

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.003005-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.003005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.003005-2
- Perl 5.22 rebuild

* Mon Mar 23 2015 Paul Howarth <paul@city-fan.org> - 1.003005-1
- Update to 1.003005
  - Fix x_contributors metadata that was killing metacpan (see
    https://github.com/CPAN-API/cpan-api/issues/401)

* Sun Mar 15 2015 Paul Howarth <paul@city-fan.org> - 1.003004-1
- Update to 1.003004
  - Caveat added to documentation about type checking the object returned by
    new() (CPAN RT#102733)

* Mon Dec  8 2014 Paul Howarth <paul@city-fan.org> - 1.003003-1
- Update to 1.003003
  - Ensure an old Cpanel::JSON::XS is upgraded if it is too old, as it will
    always be used in preference to JSON::XS
  - Avoid "JSON::XS::Boolean::* redefined" warnings caused by an old JSON::XS
    loaded at the same time as a newer Cpanel::JSON::XS

* Sun Nov 16 2014 Paul Howarth <paul@city-fan.org> - 1.003002-1
- Update to 1.003002
  - Correctly fix boolean interoperability with older Cpanel::JSON::MaybeXS

* Thu Nov 13 2014 Paul Howarth <paul@city-fan.org> - 1.003001-1
- Update to 1.003001
  - Add :legacy tag to support legacy apps
  - Fix boolean interoperability with older Cpanel::JSON::MaybeXS

* Wed Oct 22 2014 Paul Howarth <paul@city-fan.org> - 1.002006-1
- Update to 1.002006
  - Add some additional test diagnostics, to help find bad version combinations
    of JSON backends

* Wed Oct 15 2014 Paul Howarth <paul@city-fan.org> - 1.002005-1
- Update to 1.002005
  - Fix "can I haz XS?" logic precedence in Makefile.PL
  - Added the ':all' export tag
  - Removed dependency on Safe::Isa
  - Repository moved to git://git.shadowcat.co.uk/p5sagit/JSON-MaybeXS.git

* Sun Oct 12 2014 Paul Howarth <paul@city-fan.org> - 1.002004-1
- Update to 1.002004
  - Support use of PUREPERL_ONLY in Makefile.PL to avoid adding an XS
    dependency
  - New is_bool() interface

* Wed Oct  8 2014 Paul Howarth <paul@city-fan.org> - 1.002003-1
- Update to 1.002003
  - Document how to use booleans

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.002002-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May  9 2014 Paul Howarth <paul@city-fan.org> - 1.002002-2
- Sanitize for Fedora submission

* Thu Apr 24 2014 Paul Howarth <paul@city-fan.org> - 1.002002-1
- Update to 1.002002
  - More metadata fiddling, to remove the Cpanel::JSON::XS dependency visible
    to static analyzers (the prerequisites at install time remain unchanged)

* Wed Apr 23 2014 Paul Howarth <paul@city-fan.org> - 1.002001-1
- Update to 1.002001
  - Fix installation on older perls with an older ExtUtils::MakeMaker
    (CPAN RT#94964)
- Update patch for building with Test::More < 0.88

* Wed Apr 23 2014 Paul Howarth <paul@city-fan.org> - 1.002000-1
- Initial RPM version
