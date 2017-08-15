Name:           perl-List-AllUtils
Version:        0.14
Release:        1%{?dist}
Summary:        Combines List::Util, List::SomeUtils and List::UtilsBy in one bite-sized package

License:        GPL
URL:            https://metacpan.org/release/List-AllUtils
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/List-AllUtils-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
# Remove "BuildRequires:  perl-devel" for noarch packages (unneeded)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
# Correct for lots of packages, other common choices include eg. Module::Build
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Combines List::Util, List::SomeUtils and List::UtilsBy in one bite-sized package


%prep
%setup -q -n List-AllUtils-%{version}


%build
# Remove OPTIMIZE=... from noarch packages (unneeded)
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%make_build


%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%files
%{perl_vendorlib}/*
%{_mandir}/*


%changelog
