Name: pristine-tar
Version: 1.26
Release: 1
Summary: regenerate pristine tarballs

Group: Development/Tools/Other
License: GPLv2
Url: http://kitenet.net/~joey/code/pristine-tar/
Source0: %{name}.tar.gz
BuildRequires: zlib-devel, perl, perl(ExtUtils::MakeMaker)
Requires: perl, git, xdelta < 2.0.0
Requires: perl-Pristine-Tar = %{version}

BuildRequires: fdupes

%description
Using pristine-tar you can regenerate a pristine upstream tarball using only a
small binary delta file and a copy of the source which can be a revision
control checkout.

The package also includes a pristine-gz command, which can regenerate
a pristine .gz file.

The delta file is designed to be checked into revision control along-side
the source code, thus allowing the original tarball to be extracted from
revision control.

pristine-tar is available in git at git://git.kitenet.net/pristine-tar/

%package -n perl-Pristine-Tar
Summary: Perl modules for pristine-tar

%description -n perl-Pristine-Tar
Perl modules for pristine-tar split out to separate package

%prep
%setup -q -n src

%build
perl Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix}
make %{?_smp_mflags} ZGZ_LIB=%{_libdir}/zgz


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT ZGZ_LIB=%{_libdir}/zgz
chmod -x $RPM_BUILD_ROOT%{_libdir}/zgz/suse-bzip2/libbz2.a
rm -rf $RPM_BUILD_ROOT%{_libdir}/perl5/vendor_perl/*/*/auto/Pristine
rm -rf $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod

%fdupes $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc GPL TODO delta-format.txt
%{_bindir}/*
%{_mandir}/man1/*
%{_libdir}/zgz

%files -n perl-Pristine-Tar
%defattr(-,root,root,-)
%dir %{perl_vendorlib}/Pristine
%dir %{perl_vendorlib}/Pristine/Tar
%{perl_vendorlib}/*
