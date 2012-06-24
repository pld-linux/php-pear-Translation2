%include	/usr/lib/rpm/macros.php
%define		_class		Translation2
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - class for multilingual applications management
Summary(pl):	%{_pearname} - klasa do zarz�dzania wersjami j�zykowymi aplikacji
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
Ta klasa dostarcza �atwego w u�yciu sposobu do wydobywania ci�g�w
znak�w dla stron wieloj�zycznych z podanego �r�d�a danych (np. bazy
danych). Na chwil� obecn� dost�pne s� kontenery PEAR::DB oraz
PEAR::MDB - inne b�d� dost�pne w niedalekiej przysz�o�ci. Klasa
zosta�a zaprojektowana tak, aby ogranicza� liczb� zapyta� do bazy
danych, oraz buforowania wynik�w o ile jest to mo�liwe. Za pomoc�
klasy Admin mo�liwe jest �atwe i wygodne zarz�dzanie t�umaczeniami
(dodawanie/usuwanie j�zyk�w b�d� poszczeg�lnych t�umacze�).

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
