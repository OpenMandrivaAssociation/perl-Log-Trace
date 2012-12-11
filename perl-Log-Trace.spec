%define upstream_name    Log-Trace
%define upstream_version 1.070

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A guide to using Log::Trace
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
A module to provide a unified approach to tracing. A script can 'use
Log::Trace qw( < mode > )' to set the behaviour of the TRACE function.

By default, the trace functions are exported to the calling package only.
You can export the trace functions to other packages with the 'Deep'
option. See the "OPTIONS" manpage for more information.

All exports are in uppercase (to minimise collisions with "real"
functions).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.70.0-3mdv2011.0
+ Revision: 658535
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-2mdv2011.0
+ Revision: 552178
- rebuild

* Fri Jul 10 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 394296
- import perl-Log-Trace


* Fri Jul 10 2009 cpan2dist 1.070-1mdv
- initial mdv release, generated with cpan2dist
