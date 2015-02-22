# Import froms Stella7, Thx to Nux.
%define _desktopdir %{_datadir}/applications
%define _iconsdir %{_datadir}/icons
%define debug_package	%{nil}

Name:           centerim5
Version:        5.0.0beta2
Release:        0.1

Summary:        Text mode menu- and window-driven IM

Group:          Networking/Instant messaging
License:        GPLv2+
URL:            http://www.centerim.org/
Source0:        http://www.centerim.org/download/cim5/%{name}-%{version}.tar.gz
Source1:        centerim5.svg
Source2:        centerim5.desktop
Source100:	centerim5.rpmlintrc


BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  gettext-devel
BuildRequires:  gpgme-devel
BuildRequires:  pkgconfig(libssl)
BuildRequires:  jpeg-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  %{_lib}ncursesw6


Requires:       %{_lib}purple0
Requires:       xdg-utils


# let's not obsolete anything yet, version 4 still works
#Provides:       centericq = %{version}
#Obsoletes:      centericq <= 4
#Provides:	centerim
#Obsoletes:	centerim

%description
CenterIM5 is a text mode menu and window-driven IM interface that supports
the ICQ2000, Yahoo!, MSN, AIM TOC, IRC, Gadu-Gadu and Jabber protocols.
Internal RSS reader and a client for LiveJournal are provided.


%prep
%setup -q
perl -pi -e "s|ncursesw5-config|ncursesw6-config|" configure

%build
%configure 

%make


%install
%makeinstall_std

# remove unnecessary stuff
rm -f %{_libdir}/%{name}/*a

install -d %{buildroot}%{_iconsdir}
install -m 644 %{SOURCE1} %{buildroot}%{_iconsdir}
desktop-file-install \
	--dir=%{buildroot}%{_desktopdir} \
    %{SOURCE2}

find %{buildroot} -name "*.debug" -delete

%find_lang %{name}


%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS COPYING ChangeLog HACKING NEWS README TODO
%{_bindir}/%{name}
%{_libdir}/*
%{_desktopdir}/*
%{_iconsdir}/*
%{_mandir}/man1/%{name}.1.*

%changelog
* Mon May 05 2014 Nux <rpm@li.nux.ro> - 5.0.0beta2-2
- upgrade to beta2

* Mon Oct 08 2012 Nux <rpm@li.nux.ro> - 5.0.0beta1-1
- initial rpm package for centerim5
