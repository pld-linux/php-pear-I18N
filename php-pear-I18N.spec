%include	/usr/lib/rpm/macros.php
%define		_class		I18N
%define		_status		beta

%define		_pearname	%{_class}
Summary:	%{_pearname} - Internationalization package
Summary(pl):	%{_pearname} - Pakiet wspomagaj±cy umiêdzynarodowienie
Name:		php-pear-%{_pearname}
Version:	0.8.6
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8cc7870da2844ac08abf7e6a77685054
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define              _noautoreq      'pear(Translate)'

%description
This package supports you to localize your applications. Currently
multiple ways of supporting translation are implemented and methods to
determine the current users (browser-)language.

This class has in PEAR status: %{_status}.

%description -l pl
Ten pakiet pozwoli ci zlokalizowaæ twoje aplikacje. Aktualnie wiele
sposobów na wspieranie jêzyków jest zaimplementowanych oraz metod do
okre¶lania jêzyka/przegl±darki aktualnego u¿ytkowanika.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{Messages,Common}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/Messages/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Messages
install %{_pearname}-%{version}/Common/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Common

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Messages/
%dir %{php_pear_dir}/%{_class}/Common/
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Messages/*.php
%{php_pear_dir}/%{_class}/Common/*.php
