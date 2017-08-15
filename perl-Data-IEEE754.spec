Name:           perl-Data-IEEE754
Version:        0.02
Release:        1%{?dist}
Summary:        perl module for converting the internal IEEE-754 floating point values into a human-readable interpretation of the underlying data 
License:        GPL

Group:          Development/Libraries
URL:            http://metacpan.org/release/Data-IEEE754
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/Data-IEEE754-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
perl module for converting the internal IEEE-754 floating point values into a human-readable interpretation of the underlying data

%prep
%setup -q -n Data-IEEE754-%{version}

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
%{_mandir}/man3/*

%changelog
