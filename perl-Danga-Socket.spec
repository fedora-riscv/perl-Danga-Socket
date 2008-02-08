Name:           perl-Danga-Socket
Version:        1.57
Release:        3%{?dist}
Summary:        Event loop and event-driven async socket base class
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Danga-Socket/
Source0:        http://www.cpan.org/modules/by-module/Danga/Danga-Socket-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker) perl(Test::More) perl(Sys::Syscall)
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
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 07 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.57-3
- rebuild for new perl

* Wed May 07 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.57-2
- Include examples in %%doc
* Mon May 07 2007 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.57-1
- Initial import
