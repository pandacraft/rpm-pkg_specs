Name:           perl-Clone-PP
Version:        1.07
Release:        1%{?dist}
Summary:        Recursively copy Perl datatypes 
License:        GPL

Group:          Development/Libraries
URL:            http://metacpan.org/release/Clone-PP
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Clone-PP-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides a general-purpose clone function to make deep copies of Perl data structures. It calls itself recursively to copy nested hash, array, scalar and reference types, including tied variables and objects.

%prep
%setup -q -n Clone-PP-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%files
%defattr(-,root,root,-)
%defattr(-,root,root,-)
%{_datadir}/perl5/vendor_perl/*
%{_mandir}/man3/*.3*

%changelog
