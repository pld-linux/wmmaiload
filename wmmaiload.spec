Summary:	A dockapp to monitor mailboxes
Summary(pl):	Aplet monitoruj�cy skrzynki pocztowe
Name:		wmmaiload
Version:	1.0.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://tnemeth.free.fr/projets/programmes/%{name}-%{version}.tar.gz
# Source0-md5:	e19a5cfa4eb5ea7b28c7818f6ff35b95
Source1:	%{name}.desktop
URL:		http://tnemeth.free.fr/projets/dockapps.html
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WMMaiLoad is a program to monitor mailboxes. It is a dockapp that is
supported by window menagers such as Window Maker, AfterStep,
BlackBox, and Enlightenment. It has an LCD look-alike user interface.
The new mails number is displayed in the top half and the total mails
number is in the bottom half. If there is new mail, an alarm-mode will
alert you by turning on and off back-light.

%description -l pl
WMMailLoad jest programem monitoruj�cym skrzynki pocztowe. Jest to
aplet wspierany przez takich zarz�dc�w okien jak Window Maker,
AfterStep, BlackBox i Enlightenment. Posiada interfejs u�ytkownika
podobny do wy�wietlacza LCD. Liczba nowych list�w jest wy�wietlana w
g�rnej cz�ci a ca�kowita liczba list�w w dolnej po�owie. Je�eli
pojawi si� nowy list, to tryb alarmowy ostrze�e o tym poprzez
w��czanie i wy��czanie tylnego pod�wietlenia.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/docklets/*
