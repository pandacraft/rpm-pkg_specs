Name:           perl-Data-Printer
Version:        0.40
Release:        1%{?dist}
Summary:        colored pretty-print of Perl data structures and objects 
License:        GPL

Group:          Development/Libraries
URL:            http://metacpan.org/release/Data-Printer
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GARU/Data-Printer-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Data::Printer - colored pretty-print of Perl data structures and objects

%prep
%setup -q -n Data-Printer-%{version}

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
%{_datadir}/perl5/vendor_perl/*
%{_mandir}/man3/*


%changelog
