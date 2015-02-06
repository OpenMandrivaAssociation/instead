Name:		instead
Version:	1.9.0
Release:	2
Summary:	Simply text adventures/visual novels engine and game
License:	GPLv2
Group:		Games/Adventure
URL:		http://instead.googlecode.com
Source0:	http://instead.googlecode.com/files/%{name}_%{version}.tar.gz
Patch0:		instead-desktop.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(zlib)
Requires:	instead-launcher

%description
Simply text adventures/visual novels engine and game.

It was designed to interpret games that are the mix of visual novels,
text quests and classical 90'ss quests.

%prep
%setup -q
%patch0 -p1

%build
%setup_compile_flags
echo 2 | ./configure.sh
%make PREFIX=/usr

%install
%makeinstall_std PREFIX=/usr

%files
%doc doc/*
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/*/%{name}.*

