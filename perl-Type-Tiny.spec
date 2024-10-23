%define	modname	Type-Tiny
%define	modver	1.014000

Summary:	Tiny, yet Moo(se) compatible type constraint for Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		https://metacpan.org/pod/Type::Tiny
Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TOBYINK/Type-Tiny-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Exporter::Tiny)
BuildRequires:	perl(Math::BigFloat)
BuildRequires:	perl(Text::Balanced)
BuildRequires:	perl-devel

%description
Tiny, yet Moo(se) compatible type constraint for Perl

%prep
%autosetup -n %{modname}-%{modver} -p1

%build
%__perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorlib}/Devel/TypeTiny
%{perl_vendorlib}/Error/TypeTiny*
%{perl_vendorlib}/Eval/TypeTiny*
# We don't ship perl-Reply (yet)
# Package the plugin if we ever do.
%exclude %{perl_vendorlib}/Reply/Plugin/TypeTiny*
%{perl_vendorlib}/Test/TypeTiny*
%{perl_vendorlib}/Type
%{perl_vendorlib}/Types
%{_mandir}/man3*/*
