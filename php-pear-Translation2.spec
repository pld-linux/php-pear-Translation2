%include	/usr/lib/rpm/macros.php
%define		_class		Translation2
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - class for multilingual applications management
Summary(pl):	%{_pearname} - klasa do zarz±dzania wersjami jêzykowymi aplikacji
Name:		php-pear-%{_pearname}
Version:	2.0.0
%define	_version 2.0.0beta1
Release:	0.beta
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{_version}.tgz
# Source0-md5:	a656170f1f11b48158d695e6f28c2d40
URL:		http://pear.php.net/package/Translation2/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides an easy way to retrieve all the strings for a
multilingual site from a data source (i.e. db). A PEAR::DB and a
PEAR::MDB container are provided, more containers will follow. It is
designed to reduce the number of queries to the db, caching the
results when possible. An Admin class is provided to easily manage
translations (add/remove a language, add/remove a string).

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa dostarcza ³atwego w u¿yciu sposobu do wydobywania ci±gów
znaków dla stron wielojêzycznych z podanego ¼ród³a danych (np. bazy
danych). Na chwilê obecn± dostêpne s± kontenery PEAR::DB oraz
PEAR::MDB - inne bêd± dostêpne w niedalekiej przysz³o¶ci. Klasa
zosta³a zaprojektowana tak, aby ograniczaæ liczbê zapytañ do bazy
danych, oraz buforowania wyników o ile jest to mo¿liwe. Za pomoc±
klasy Admin mo¿liwe jest ³atwe i wygodne zarz±dzanie t³umaczeniami
(dodawanie/usuwanie jêzyków b±d¼ poszczególnych t³umaczeñ).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{Admin/Container,Container}

install %{_pearname}-%{_version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{_version}/Admin/Container/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Admin/Container
install %{_pearname}-%{_version}/Container/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Container

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{_version}/docs
%{php_pear_dir}/%{_class}
