#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-CPAN-Meta-Check
Version  : 0.014
Release  : 21
URL      : http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/CPAN-Meta-Check-0.014.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/CPAN-Meta-Check-0.014.tar.gz
Summary  : 'Verify requirements in a CPAN::Meta object'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-CPAN-Meta-Check-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Deep)

%description
This archive contains the distribution CPAN-Meta-Check,
version 0.014:
Verify requirements in a CPAN::Meta object

%package dev
Summary: dev components for the perl-CPAN-Meta-Check package.
Group: Development
Provides: perl-CPAN-Meta-Check-devel = %{version}-%{release}

%description dev
dev components for the perl-CPAN-Meta-Check package.


%package license
Summary: license components for the perl-CPAN-Meta-Check package.
Group: Default

%description license
license components for the perl-CPAN-Meta-Check package.


%prep
%setup -q -n CPAN-Meta-Check-0.014

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-CPAN-Meta-Check
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-CPAN-Meta-Check/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1CPAN/Meta/Check.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CPAN::Meta::Check.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-CPAN-Meta-Check/LICENSE
