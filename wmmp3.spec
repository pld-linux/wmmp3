Summary:	wmmp3 - mpg123 frontend for the WindowMaker Dock
Summary(pl):	wmmp3 - nak³adka na mpg123 dla Doku WindowMakera
Name:		wmmp3
Version:	0.11
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dotfiles.com/software/wmmp3/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-mpg123_path.patch
URL:		http://dotfiles.com/software/wmmp3/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	mpg123
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix 	/usr/X11R6

%description
wmmp3 is a frontend for the mpg123 mp3 player. It is an X11
application designed to work in the WindowMaker dock. All user options
are contained in a config file, $CONFIG_DIR/wmmp3 . There is a
sample.wmmp3 file in the package that can be used as an
example/template.

%description -l pl
wmmp3 jest nak³adk± dla odtwarzacza mp3 - mpg123, zaprojektowan± do
pracy w Doku WindowMakera. Wszystkie opcje u¿ytkownika s± zawarte w
pliku $CONFIG_DIR/wmmp3. W pakiecie znajduje siê plik sample.wmmp3,
mog±cy pos³u¿yæ za przyk³ad lub szablon do stworzenia w³asnego pliku
konfiguracyjnego.

%prep
%setup -q
%patch0 -p1
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
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf README TODO ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz sample.wmmp3
%attr(755,root,root) %{_bindir}/wmmp3

#%{_applnkdir}/DockApplets/wmmp3.desktop
