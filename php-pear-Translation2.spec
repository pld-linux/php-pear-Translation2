%define		_status		stable
%define		_pearname	Translation2
Summary:	%{_pearname} - class for multilingual applications management
Summary(pl.UTF-8):	%{_pearname} - klasa do zarządzania wersjami językowymi aplikacji
Name:		php-pear-%{_pearname}
Version:	2.0.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	40dde8c51d7edaa443b339444b999941
URL:		http://pear.php.net/package/Translation2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Suggests:	php-gettext
Suggests:	php-pear-Cache_Lite
Suggests:	php-pear-DB
Suggests:	php-pear-DB_DataObject
Suggests:	php-pear-File_Gettext
Suggests:	php-pear-I18Nv2
Suggests:	php-pear-MDB
Suggests:	php-pear-MDB2
Suggests:	php-pear-XML_Serializer
Obsoletes:	php-pear-Translation2-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Cache/Lite.*) pear(DB.*) pear(DB/DataObject.*) pear(MDB.*) pear(MDB2.*) pear(gettext.*) pear(File/Gettext.*) pear(I18Nv2.*) pear(XML/Serializer.*)

%description
This class provides an easy way to retrieve all the strings for a
multilingual site from a data source (i.e. db). A PEAR::DB and a
PEAR::MDB container are provided, more containers will follow. It is
designed to reduce the number of queries to the db, caching the
results when possible. An Admin class is provided to easily manage
translations (add/remove a language, add/remove a string).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa dostarcza łatwego w użyciu sposobu do wydobywania ciągów
znaków dla stron wielojęzycznych z podanego źródła danych (np. bazy
danych). Na chwilę obecną dostępne są kontenery PEAR::DB oraz
PEAR::MDB - inne będą dostępne w niedalekiej przyszłości. Klasa
została zaprojektowana tak, aby ograniczać liczbę zapytań do bazy
danych, oraz buforowania wyników o ile jest to możliwe. Za pomocą
klasy Admin możliwe jest łatwe i wygodne zarządzanie tłumaczeniami
(dodawanie/usuwanie języków bądź poszczególnych tłumaczeń).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv docs/%{_pearname}/docs/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Translation2.php
%{php_pear_dir}/Translation2

%{_examplesdir}/%{name}-%{version}
