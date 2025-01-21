#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-CPAN-Meta-Check
Version  : 0.018
Release  : 43
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/CPAN-Meta-Check-0.018.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/CPAN-Meta-Check-0.018.tar.gz
Summary  : 'Verify requirements in a CPAN::Meta object'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-CPAN-Meta-Check-license = %{version}-%{release}
Requires: perl-CPAN-Meta-Check-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution CPAN-Meta-Check,
version 0.018:
Verify requirements in a CPAN::Meta object

%package dev
Summary: dev components for the perl-CPAN-Meta-Check package.
Group: Development
Provides: perl-CPAN-Meta-Check-devel = %{version}-%{release}
Requires: perl-CPAN-Meta-Check = %{version}-%{release}

%description dev
dev components for the perl-CPAN-Meta-Check package.


%package license
Summary: license components for the perl-CPAN-Meta-Check package.
Group: Default

%description license
license components for the perl-CPAN-Meta-Check package.


%package perl
Summary: perl components for the perl-CPAN-Meta-Check package.
Group: Default
Requires: perl-CPAN-Meta-Check = %{version}-%{release}

%description perl
perl components for the perl-CPAN-Meta-Check package.


%prep
%setup -q -n CPAN-Meta-Check-0.018
cd %{_builddir}/CPAN-Meta-Check-0.018

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-CPAN-Meta-Check
cp %{_builddir}/CPAN-Meta-Check-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-CPAN-Meta-Check/bf7229bbf443f280efe9e5614e9c41cdb67639dc || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CPAN::Meta::Check.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-CPAN-Meta-Check/bf7229bbf443f280efe9e5614e9c41cdb67639dc

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
