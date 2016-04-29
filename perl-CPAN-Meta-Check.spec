#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-CPAN-Meta-Check
Version  : 0.012
Release  : 8
URL      : http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/CPAN-Meta-Check-0.012.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/CPAN-Meta-Check-0.012.tar.gz
Summary  : 'Verify requirements in a CPAN::Meta object'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-CPAN-Meta-Check-doc

%description
This archive contains the distribution CPAN-Meta-Check,
version 0.012:
Verify requirements in a CPAN::Meta object

%package doc
Summary: doc components for the perl-CPAN-Meta-Check package.
Group: Documentation

%description doc
doc components for the perl-CPAN-Meta-Check package.


%prep
%setup -q -n CPAN-Meta-Check-0.012

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/CPAN/Meta/Check.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
