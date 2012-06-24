%include	/usr/lib/rpm/macros.php
%define		_class		Translation2
%define		_status		beta
%define		_pearname	%{_class}

%define	_beta	beta11
%define	_rel	1
Summary:	%{_pearname} - class for multilingual applications management
Summary(pl):	%{_pearname} - klasa do zarz�dzania wersjami j�zykowymi aplikacji
Name:		php-pear-%{_pearname}
Version:	2.0.0
Release:	0.%{_beta}.%{_rel}
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_beta}.tgz
# Source0-md5:	1dbe068aad9193ae708a9250c1d61ea4
URL:		http://pear.php.net/package/Translation2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Cache/Lite.*)' 'pear(DB.*)' 'pear(DB/DataObject.*)' 'pear(MDB.*)' 'pear(MDB2.*)' 'pear(gettext.*)' 'pear(File/Gettext.*)' 'pear(I18Nv2.*)' 'pear(XML/Serializer.*)'

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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}.php
%{php_pear_dir}/%{_class}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
