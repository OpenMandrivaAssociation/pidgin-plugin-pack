%define oname purple-plugin_pack
%define version 2.4.0
%define fname %oname-%version
%define pidgin_major_ver 2
%define pidgin_minor_ver 4
%define pidgin_next_major_ver %(echo $((%{pidgin_major_ver}+1)))
%define pidgin_build_minor_ver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists pidgin); then pkg-config --modversion pidgin | awk -F. '{ print $2 }'; else echo 0; fi)

Summary:    Plugin Pack for libpurple and derived IM clients
Name:       pidgin-plugin-pack
Version:    %version

Release:    %mkrel 1
License:    GPLv2+
Group:      Networking/Instant messaging

URL:        http://plugins.guifications.org/
Source0:    %{fname}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: intltool
BuildRequires: python
BuildRequires: pidgin-devel >= %{pidgin_major_ver}.%{pidgin_minor_ver}, pidgin-devel < %{pidgin_next_major_ver}
BuildRequires: gtk2-devel
BuildRequires: gtkspell-devel
Requires:   pidgin >= %{pidgin_major_ver}.%{pidgin_build_minor_ver}, pidgin < %{pidgin_next_major_ver}


%description
Additional plugins for Pidgin.

%package -n pidgin-xmms
Group: Networking/Instant messaging
Summary: Xmms control plugin for Pidgin
Requires:   pidgin >= %{pidgin_major_ver}.%{pidgin_build_minor_ver}, pidgin < %{pidgin_next_major_ver}
Requires: xmms
BuildRequires: xmms-devel

%description -n pidgin-xmms
This is a plugin for Pidgin to control the Xmms music player.

%prep
%setup -q -n %fname

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -f $RPM_BUILD_ROOT%{_libdir}/purple-2/*.la $RPM_BUILD_ROOT%{_libdir}/purple-2/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/*.la $RPM_BUILD_ROOT%{_libdir}/pidgin/*.a
%find_lang plugin_pack

%clean
rm -rf $RPM_BUILD_ROOT

%files -f plugin_pack.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog
%{_datadir}/pixmaps/pidgin/protocols/*/napster.png
%_libdir/pidgin/album.so
%_libdir/pidgin/blistops.so
%_libdir/pidgin/convbadger.so
%_libdir/pidgin/difftopic.so
%_libdir/pidgin/enhancedhist.so
%_libdir/pidgin/gRIM.so
%_libdir/pidgin/infopane.so
%_libdir/pidgin/irssi.so
%_libdir/pidgin/lastseen.so
%_libdir/pidgin/listlog.so
%_libdir/pidgin/mystatusbox.so
%_libdir/pidgin/nicksaid.so
%_libdir/pidgin/pidgin-schedule.so
%_libdir/pidgin/plonkers.so
%_libdir/pidgin/sepandtab.so
%_libdir/pidgin/switchspell.so
%_libdir/pidgin/timelog.so
%_libdir/pidgin/xchat-chats.so
%_libdir/purple-2/autoprofile.so
%_libdir/purple-2/autoreply.so
%_libdir/purple-2/bash.so
%_libdir/purple-2/colorize.so
%_libdir/purple-2/dewysiwygification.so
%_libdir/purple-2/dice.so
%_libdir/purple-2/eight_ball.so
%_libdir/purple-2/flip.so
%_libdir/purple-2/google.so
%_libdir/purple-2/highlight.so
%_libdir/purple-2/ignore.so
%_libdir/purple-2/irchelper.so
%_libdir/purple-2/irc-more.so
%_libdir/purple-2/libsnpp.so
%_libdir/purple-2/listhandler.so
%_libdir/purple-2/napster.so
%_libdir/purple-2/oldlogger.so
%_libdir/purple-2/showoffline.so
%_libdir/purple-2/simfix.so
%_libdir/purple-2/slashexec.so
%_libdir/purple-2/splitter.so
%_libdir/purple-2/sslinfo.so

%files -n pidgin-xmms
%defattr(-,root,root,-)
%_libdir/pidgin/xmmsremote.so
%dir %{_datadir}/pixmaps/pidgin/plugin_pack
%{_datadir}/pixmaps/pidgin/plugin_pack/xmmsremote/
