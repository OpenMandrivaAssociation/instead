Name:		instead
Version:	1.6.2
Release:	%mkrel 1
Summary:	Simply text adventures/visual novels engine and game
License:	GPLv2
Group:		Games/Adventure
URL:		http://instead.googlecode.com
Source0:	http://instead.googlecode.com/files/%{name}_%{version}.tar.gz
Patch0:		instead-desktop.patch
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	lua-devel
BuildRequires:	gtk+2-devel
BuildRequires:	zlib-devel
Requires:	instead-launcher

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
%__rm -rf %{buildroot}
%makeinstall_std PREFIX=/usr

%clean
%__rm -rf %{buildroot}

%files
%doc doc/*
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/*/%{name}.*

