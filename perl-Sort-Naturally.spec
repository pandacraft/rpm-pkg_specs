Name:           perl-Sort-Naturally
Version:        1.03
Release:        1%{?dist}
Summary:        sort lexically, but sort numeral parts numerically 
License:        GPL

Group:          Development/Libraries
URL:            http://metacpan.org/release/Sort-Naturally
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Sort-Naturally-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module exports two functions, nsort and ncmp; they are used in implementing my idea of a "natural sorting" algorithm. Under natural sorting, numeric substrings are compared numerically, and other word-characters are compared lexically.

%prep
%setup -q -n Sort-Naturally-%{version}

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
%{_mandir}/man3/*.3*

%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 1.03
- Package creation for production usage on amzn 2017.03
