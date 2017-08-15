Name:           perl-List-UtilsBy
Version:        0.10
Release:        1%{?dist}
Summary:        higher-order list utility functions 
License:        GPL

Group:          Development/Libraries
URL:            http://metacpan.org/release/List-UtilsBy
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/List-UtilsBy-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides a number of list utility functions, all of which take an initial code block to control their behaviour. They are variations on similar core perl or List::Util functions of similar names, but which use the block to control their behaviour. For example, the core Perl function sort takes a list of values and returns them, sorted into order by their string value. The sort_by function sorts them according to the string value returned by the extra function, when given each value.

%prep
%setup -q -n List-UtilsBy-%{version}

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
