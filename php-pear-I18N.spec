%include	/usr/lib/rpm/macros.php
%define		_class		I18N
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - internationalization package
Summary(pl):	%{_pearname} - pakiet wspomagaj±cy umiêdzynarodowienie
Name:		php-pear-%{_pearname}
Version:	0.8.6
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8cc7870da2844ac08abf7e6a77685054
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/I18N/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'pear(Translate)'

%description
This package supports you to localize your applications. Currently
multiple ways of supporting translation are implemented and methods to
determine the current users (browser-)language.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet pozwoli ci zlokalizowaæ twoje aplikacje. Aktualnie wiele
sposobów na wspieranie jêzyków jest zaimplementowanych oraz metod do
okre¶lania jêzyka/przegl±darki aktualnego u¿ytkownika.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}/%{_class}
%patch0 -p2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/Messages/
%dir %{php_pear_dir}/%{_class}/Common/
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Messages/*.php
%{php_pear_dir}/%{_class}/Common/*.php
