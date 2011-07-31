%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Date_Holidays_Sweden
Summary:	%{_pearname} - Driver based class to calculate holidays in Sweden
Summary(pl.UTF-8):	%{_pearname} - klasa do obliczania dat świąt szwedzkich
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	58c8c5d4f02323b966a1843080713d4a
URL:		http://pear.php.net/package/Date_Holidays_Sweden/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Date_Holidays >= 0.21.1
Obsoletes:	php-pear-Date_Holidays_Sweden-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date_Holidays helps you calculate the dates and titles of holidays and
other special celebrations. This is the driver for calculating
holidays in Sweden.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Date_Holidays pozwala na obliczenie dat oraz tytułów świąt oraz
specjalnych okazji. Klasa ta pozwala na wyliczenie świąt szwedzkich.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Date/Holidays/Driver/Sweden.php
%{php_pear_dir}/data/Date_Holidays_Sweden
