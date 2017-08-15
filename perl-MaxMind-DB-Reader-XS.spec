Name:           perl-MaxMind-DB-Reader-XS
Version:        1.000004
Release:        1%{?dist}
Summary:        Fast XS implementation of MaxMind DB reader
License:        GPL

Group:          Development/Libraries
URL:            https://metacpan.org/release/MaxMind-DB-Reader-XS
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/MaxMind-DB-Reader-XS-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: perl(Math::Int128) is not installed
    !  MaxMind::DB::Metadata is not installed
    !  MaxMind::DB::Reader is not installed
    !  MaxMind::DB::Reader::Role::HasMetadata is not installed
    !  MaxMind::DB::Reader::Role::Reader is not installed
    !  MaxMind::DB::Types is not installed
    !  Moo is not installed
    !  namespace::autoclean

%{?perl_default_filter}

%description
Simply installing this module causes MaxMind::DB::Reader to use the XS implementation, which is much faster than the Perl implementation.

The XS implementation links against the libmaxminddb library.

See MaxMind::DB::Reader for API details.

%prep
%setup -q -n MaxMind-DB-Reader-XS-%{version}

%build
%{__perl} Build.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
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
