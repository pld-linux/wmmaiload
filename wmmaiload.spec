Summary:	A dockapp to monitor mailboxes
Summary(pl):	Aplet monitoruj±cy skrzynki pocztowe
Name:		wmmaiload
Version:	0.10.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://tnemeth.free.fr/projets/programmes/%{name}-%{version}.tar.gz
# Source0-md5:	aea7e5f51ec57f65a5e0009ba9ed060d
Source1:	%{name}.desktop
URL:		http://tnemeth.free.fr/projets/dockapps.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WMMaiLoad is a program to monitor mailboxes. It is a dockapp that is
supported by window menagers such as Window Maker, AfterStep,
BlackBox, and Enlightenment. It has an LCD look-alike user interface.
The new mails number is displayed in the top half and the total mails
number is in the bottom half. If there is new mail, an alarm-mode will
alert you by turning on and off back-light.

%description -l pl
WMMailLoad jest programem monitoruj±cym skrzynki pocztowe. Jest to
aplet wspierany przez takich zarz±dców okien jak Window Maker,
AfterStep, BlackBox i Enlightenment. Posiada interfejs u¿ytkownika
podobny do wy¶wietlacza LCD. Liczba nowych listów jest wy¶wietlana w
górnej czê¶ci a ca³kowita liczba listów w dolnej po³owie. Je¿eli
pojawi siê nowy list, to tryb alarmowy ostrze¿e o tym poprzez
w³±czanie i wy³±czanie tylnego pod¶wietlenia.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_applnkdir}/DockApplets/*
