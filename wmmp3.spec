Summary:	wmmp3 - mpg123 frontend for the WindowMaker Dock
Summary(pl):	wmmp3 - nak�adka na mpg123 dla Doku WindowMakera
Name:		wmmp3
Version:	0.12
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dotfiles.com/software/wmmp3/%{name}-%{version}.tar.gz
# Source0-md5:	4bbc839c48cb13680f94b2fa133ca423
Source1:	%{name}.desktop
#Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-mpg123_path.patch
URL:		http://dotfiles.com/software/wmmp3/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	mpg123
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmmp3 is a frontend for the mpg123 MP3 player. It is an X11
application designed to work in the WindowMaker dock. All user options
are contained in a config file, $CONFIG_DIR/wmmp3 . There is a
sample.wmmp3 file in the package that can be used as an
example/template.

%description -l pl
wmmp3 jest nak�adk� dla odtwarzacza MP3 - mpg123, zaprojektowan� do
pracy w Doku WindowMakera. Wszystkie opcje u�ytkownika s� zawarte w
pliku $CONFIG_DIR/wmmp3. W pakiecie znajduje si� plik sample.wmmp3,
mog�cy pos�u�y� za przyk�ad lub szablon do stworzenia w�asnego pliku
konfiguracyjnego.

%prep
%setup -q
#%%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
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
%doc README TODO ChangeLog AUTHORS sample.wmmp3
%attr(755,root,root) %{_bindir}/wmmp3
%{_desktopdir}/docklets/wmmp3.desktop
