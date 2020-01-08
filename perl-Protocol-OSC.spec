#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Protocol-OSC
Version  : 0.09
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/E/EG/EGOR/Protocol-OSC-0.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EG/EGOR/Protocol-OSC-0.09.tar.gz
Summary  : 'Open Sound Control v1.1 protocol implementation'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Protocol-OSC-license = %{version}-%{release}
Requires: perl-Protocol-OSC-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Protocol-OSC,
version 0.09:
Open Sound Control v1.1 protocol implementation

%package dev
Summary: dev components for the perl-Protocol-OSC package.
Group: Development
Provides: perl-Protocol-OSC-devel = %{version}-%{release}
Requires: perl-Protocol-OSC = %{version}-%{release}

%description dev
dev components for the perl-Protocol-OSC package.


%package license
Summary: license components for the perl-Protocol-OSC package.
Group: Default

%description license
license components for the perl-Protocol-OSC package.


%package perl
Summary: perl components for the perl-Protocol-OSC package.
Group: Default
Requires: perl-Protocol-OSC = %{version}-%{release}

%description perl
perl components for the perl-Protocol-OSC package.


%prep
%setup -q -n Protocol-OSC-0.09
cd %{_builddir}/Protocol-OSC-0.09

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Protocol-OSC
cp %{_builddir}/Protocol-OSC-0.09/LICENSE %{buildroot}/usr/share/package-licenses/perl-Protocol-OSC/9eb5e858145b1631787f5955d00e832950b9463c
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
/usr/share/man/man3/Protocol::OSC.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Protocol-OSC/9eb5e858145b1631787f5955d00e832950b9463c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/Protocol/OSC.pm
/usr/lib/perl5/vendor_perl/5.30.1/Protocol/OSC.pod
