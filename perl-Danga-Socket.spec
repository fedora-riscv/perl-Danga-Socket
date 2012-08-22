Name:           perl-Danga-Socket
Version:        1.61
Release:        5%{?dist}
Summary:        Event loop and event-driven async socket base class
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Danga-Socket/
Source0:        http://www.cpan.org/modules/by-module/Danga/Danga-Socket-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker) perl(Test::More) perl(Sys::Syscall)
BuildRequires:  perl(Time::HiRes)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is an abstract base class for objects backed by a socket which
provides the basic framework for event-driven asynchronous IO, designed to
be fast. Danga::Socket is both a base class for objects, and an event loop.

%prep
%setup -q -n Danga-Socket-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%defattr(-,root,root,-)
%doc CHANGES examples/
%{perl_vendorlib}/Danga
%{_mandir}/man3/Danga::Socket.*

%changelog
* Tue Aug 21 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.61-5
- Explicitly BuildRequire Time::HiRes, so the test suite passes
- Use the "Danga" name in the files listing, to match Rawhide

* Wed Aug 01 2012 Luis Bazan <lbazan@fedoraproject.org> - 1.61-4
- changes lib root

* Wed Aug 01 2012 Luis Bazan <lbazan@fedoraproject.org> - 1.61-3
- rebuild againts to check log

* Tue Jul 31 2012 Luis Bazan <lbazan@fedoraproject.org> - 1.61-2
- Fix dependency

* Fri Jun 22 2012 Luis Bazan <lbazan@fedoraproject.org> - 1.61-1 
- Upstream released new version

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.58-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.58-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.58-1
- 1.58

* Thu Feb 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.57-3
- rebuild for new perl

* Wed May 07 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.57-2
- Include examples in %%doc
* Mon May 07 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.57-1
- Initial import
