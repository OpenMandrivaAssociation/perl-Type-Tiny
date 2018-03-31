%define	modname	Type-Tiny
%define	modver	1.002001

Summary:	Tiny, yet Moo(se) compatible type constraint for Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/Type-Tiny-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Tiny, yet Moo(se) compatible type constraint for Perl

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Devel/TypeTiny
%{perl_vendorlib}/Error/TypeTiny*
%{perl_vendorlib}/Eval/TypeTiny*
%{perl_vendorlib}/Reply/Plugin/TypeTiny*
%{perl_vendorlib}/Test/TypeTiny*
%{perl_vendorlib}/Type
%{perl_vendorlib}/Types
%{_mandir}/man3*/*
