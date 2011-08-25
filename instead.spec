%define	name	instead
%define	version	1.5.0
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
URL:		http://instead.googlecode.com
Source0:	http://instead.googlecode.com/files/%{name}_%{version}.tar.gz
Patch0:		instead-1.5.0-desktop.patch
Group:		Games/Adventure
Summary:	Simply text adventures/visual novels engine and game

Requires: instead-launcher

BuildRequires: SDL-devel
BuildRequires: SDL_mixer-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_ttf-devel
BuildRequires: lua-devel
BuildRequires: gtk+2-devel
BuildRequires: zlib-devel

%description 
Simply text adventures/visual novels engine and game.

It was designed to interpret games that are the mix of visual novels,
text quests and classical 90'ss quests.

%prep
%setup -q
%patch0 -p1

%build
echo 2 | ./configure.sh
%make PREFIX=/usr

%install
%makeinstall_std PREFIX=/usr

%files
%defattr(-,root,root,-)
%doc doc/*
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/*/%{name}.*

