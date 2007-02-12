Summary:	A dockapp to monitor mailboxes
Summary(pl.UTF-8):	Aplet monitorujący skrzynki pocztowe
Name:		wmmaiload
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://tnemeth.free.fr/projets/programmes/%{name}-%{version}.tar.gz
# Source0-md5:	bf4d0274a99a610d2f22442a06903eec
Source1:	%{name}.desktop
URL:		http://tnemeth.free.fr/projets/dockapps.html
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WMMaiLoad is a program to monitor mailboxes. It is a dockapp that is
supported by window menagers such as Window Maker, AfterStep,
BlackBox, and Enlightenment. It has an LCD look-alike user interface.
The new mails number is displayed in the top half and the total mails
number is in the bottom half. If there is new mail, an alarm-mode will
alert you by turning on and off back-light.

%description -l pl.UTF-8
WMMailLoad jest programem monitorującym skrzynki pocztowe. Jest to
aplet wspierany przez takich zarządców okien jak Window Maker,
AfterStep, BlackBox i Enlightenment. Posiada interfejs użytkownika
podobny do wyświetlacza LCD. Liczba nowych listów jest wyświetlana w
górnej części a całkowita liczba listów w dolnej połowie. Jeżeli
pojawi się nowy list, to tryb alarmowy ostrzeże o tym poprzez
włączanie i wyłączanie tylnego podświetlenia.

%prep
%setup -q

%build
cp -f %{_datadir}/automake/config.sub .
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
%doc AUTHORS ChangeLog NEWS README TODO THANKS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/docklets/*
