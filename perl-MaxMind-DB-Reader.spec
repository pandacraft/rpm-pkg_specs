Name:           perl-MaxMind-DB-Reader
Version:        1.000013
Release:        1%{?dist}
Summary:        Read MaxMind DB files and look up IP addresses
License:        GPL

Group:          Development/Libraries
URL:            https://metacpan.org/release/MaxMind-DB-Reader
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/MaxMind-DB-Reader-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module adds support for MaxMind database reading

%prep
%setup -q -n MaxMind-DB-Reader-%{version}

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
%{_bindir}/mmdb-dump-metadata
%{_bindir}/mmdb-dump-search-tree
%{_datadir}/man/man3/*
%{_datadir}/perl5/vendor_perl/*

%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 1.000013
- Package creation for production usage on amzn 2017.03
