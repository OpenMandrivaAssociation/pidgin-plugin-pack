%define oname purple-plugin_pack
%define version 1.0
%define prerel beta7
%define fname %oname-%version%prerel
%define pidgin_major_ver 2
%define pidgin_minor_ver 0
%define pidgin_next_major_ver %(echo $((%{pidgin_major_ver}+1)))
%define pidgin_build_minor_ver %(pkg-config --modversion pidgin | awk -F. '{ print $2 }')

Summary:    Plugin Pack for libpurple and derived IM clients
Name:       pidgin-plugin-pack
Version:    %version

Release:    %mkrel 0.%prerel.1
License:    GPL
Group:      Networking/Instant messaging

URL:        http://plugins.guifications.org/
Source0:    %{fname}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl-XML-Parser
BuildRequires: xmms-devel
BuildRequires: pidgin-devel >= %{pidgin_major_ver}.%{pidgin_minor_ver}, pidgin-devel < %{pidgin_next_major_ver}
BuildRequires: gtk2-devel
Requires:   pidgin >= %{pidgin_major_ver}.%{pidgin_build_minor_ver}, pidgin < %{pidgin_next_major_ver}

%description
Additional plugins for Pidgin.

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
%_libdir/pidgin/album.so
%_libdir/pidgin/blistops.so
%_libdir/pidgin/difftopic.so
%_libdir/pidgin/gRIM.so
%_libdir/pidgin/hideconv.so
%_libdir/pidgin/irssi.so
%_libdir/pidgin/lastseen.so
%_libdir/pidgin/mystatusbox.so
%_libdir/pidgin/nicksaid.so
%_libdir/pidgin/pidgin-schedule.so
%_libdir/pidgin/plonkers.so
%_libdir/pidgin/sepandtab.so
%_libdir/pidgin/xchat-chats.so
%_libdir/pidgin/xmmsremote.so
%_libdir/purple-2/autoreply.so
%_libdir/purple-2/bash.so
%_libdir/purple-2/dice.so
%_libdir/purple-2/eight_ball.so
%_libdir/purple-2/flip.so
%_libdir/purple-2/irchelper.so
%_libdir/purple-2/listhandler.so
%_libdir/purple-2/oldlogger.so
%_libdir/purple-2/showoffline.so
%_libdir/purple-2/simfix.so
%_libdir/purple-2/slashexec.so
%_libdir/purple-2/sslinfo.so
%{_datadir}/pixmaps/pidgin/plugin_pack
