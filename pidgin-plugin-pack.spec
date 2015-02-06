%define oname purple-plugin_pack
%define version 2.6.3
%define fname %oname-%version
%define pidgin_major_ver 2
%define pidgin_minor_ver 6
%define pidgin_next_major_ver %(echo $((%{pidgin_major_ver}+1)))
%define pidgin_build_minor_ver %(if $([ -x %{_bindir}/pkg-config ] && pkg-config --exists pidgin); then pkg-config --modversion pidgin | awk -F. '{ print $2 }'; else echo 0; fi)

Summary:    Plugin Pack for libpurple and derived IM clients
Name:       pidgin-plugin-pack
Version:    %version

Release:    4
License:    GPLv2+
Group:      Networking/Instant messaging

URL:        http://plugins.guifications.org/
Source0:    %{fname}.tar.bz2
BuildRequires: intltool
BuildRequires: python
BuildRequires: pidgin-devel >= %{pidgin_major_ver}.%{pidgin_minor_ver}, pidgin-devel < %{pidgin_next_major_ver}
BuildRequires: gtk2-devel
BuildRequires: gtkspell-devel
BuildRequires: talkfilters-devel
Requires:   pidgin >= %{pidgin_major_ver}.%{pidgin_build_minor_ver}, pidgin < %{pidgin_next_major_ver}


%description
Additional plugins for Pidgin.

%prep
%setup -q -n %fname

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang plugin_pack

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
%_libdir/pidgin/talkfilters.so
%_libdir/pidgin/timelog.so
%_libdir/pidgin/xchat-chats.so
%_libdir/purple-2/autoprofile.so
%_libdir/purple-2/autoreply.so
%_libdir/purple-2/bash.so
%_libdir/purple-2/colorize.so
%_libdir/purple-2/dewysiwygification.so
%_libdir/purple-2/dice.so
%_libdir/purple-2/eight_ball.so
%_libdir/purple-2/findip.so
%_libdir/purple-2/flip.so
%_libdir/purple-2/google.so
%_libdir/purple-2/groupmsg.so
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
%_libdir/purple-2/xmppprio.so


%changelog
* Tue Jul 26 2011 Götz Waschk <waschk@mandriva.org> 2.6.3-2mdv2012.0
+ Revision: 691702
- rebuild

* Sun Jul 25 2010 Götz Waschk <waschk@mandriva.org> 2.6.3-1mdv2011.0
+ Revision: 558536
- new version

* Wed Jan 20 2010 Götz Waschk <waschk@mandriva.org> 2.6.2-1mdv2010.1
+ Revision: 494041
- new version
- readd talkfilters plugin

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 2.6.0-2mdv2010.1
+ Revision: 460851
- new version
- drop patch
- update file list

* Mon Apr 20 2009 Götz Waschk <waschk@mandriva.org> 2.5.1-2mdv2010.0
+ Revision: 368373
- fix very slow tab switching with switchspell enabled

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 2.5.1-1mdv2009.1
+ Revision: 323291
- New version 2.5.1

* Tue Aug 05 2008 Götz Waschk <waschk@mandriva.org> 2.4.0-1mdv2009.0
+ Revision: 264082
- update build deps
- new version
- remove talkfilters plugin
- add new plugins: autoprofile, colorize, google, listlog, splitter

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 2.3.0-1mdv2009.0
+ Revision: 192441
- new version
- drop patch
- update file list

* Mon Mar 03 2008 Götz Waschk <waschk@mandriva.org> 2.2.0-2mdv2008.1
+ Revision: 177960
- patch to fix timelog plugin

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 05 2007 Götz Waschk <waschk@mandriva.org> 2.2.0-1mdv2008.1
+ Revision: 106112
- new version
- update plugin list

* Wed Oct 03 2007 Funda Wang <fwang@mandriva.org> 2.1.1-2mdv2008.0
+ Revision: 95067
- rebuild against pidgin 2.2.1

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 2.1.1-1mdv2008.0
+ Revision: 72700
- new version
- update file list

* Fri Jul 20 2007 Götz Waschk <waschk@mandriva.org> 2.0.0-1mdv2008.0
+ Revision: 53860
- fix version macro in the spec file
- new version
- add new plugins
- update buildrequires

* Sun Jun 03 2007 Götz Waschk <waschk@mandriva.org> 1.0-1mdv2008.0
+ Revision: 34951
- new version

* Thu May 03 2007 Götz Waschk <waschk@mandriva.org> 1.0-0.beta7.2mdv2008.0
+ Revision: 20867
- split out xmms package

* Wed May 02 2007 Götz Waschk <waschk@mandriva.org> 1.0-0.beta7.1mdv2008.0
+ Revision: 20766
- Import pidgin-plugin-pack




* Wed May  2 2007 Götz Waschk <waschk@mandriva.org> 1.0-0.beta7.1mdv2008.0
- initial package

* Mon Apr 30 2007 Stu Tomlinson <stu@nosnilmot.com>
- Update for the rename of Gaim to Pidgin
- New URL for our new website
- Use tar.bz2 for source
- Split into pidgin- and purple- RPMs

* Tue Dec 5 2006 John Bailey <rekkanoryo@rekkanoryo.org>
- Update the URL to match our new website

* Thu Oct 19 2006 Stu Tomlinson <stu@nosnilmot.com>
- Removed locale from %%files, that's what %%find_lang is for
- Fixed finding translations
- Fixed %%s in %%changelog
- Package xmms pixmaps
- Add xmms-devel buildrequires

* Sun Nov 11 2005 Peter Lawler <bleeter from users.sf.net>
- Added locale to %%files
- Enabled %%find_lang

* Thu Nov 03 2005 Stu Tomlinson <stu@nosnilmot.com>
- Fix it again

* Wed Nov 02 2005 Peter Lawler <bleeter@users.sf.net>
- Fixed up the Mandrivel .so rename

* Tue Nov 01 2005 Stu Tomlinson <stu@nosnilmot.com>
- Fix it

* Tue Nov 01 2005 Peter Lawler <bleeter@users.sf.net>
- Initial Spec File for Plugin Pack
