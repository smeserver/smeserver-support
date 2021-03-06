# $Id: smeserver-support.spec,v 1.37 2010/07/13 18:09:10 slords Exp $

Summary: SME Server module to display support and licensing information
%define name smeserver-support
Name: %{name}
%define version 2.2.0
%define release 18

# These packages come from CentOS, but wee need to use care when
# updating them - either we've patched them, or we need to do something
# prior to taking the update

# TODO: check mkinitrd,mdadm to see if needed
%define centos_excludes initscripts,libgsf
%define centos_remove   kernel,kernel-smp,kernel-xenU,mkinitrd,mdadm

Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Source1: smeserver_logo.jpg
Source2: smeserver_logo.gif
Patch0: smeserver-support.bug5656.patch
Patch1: smeserver-support-2.2.0-migrate_excludes.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools >= 1.7.5
BuildArchitectures: noarch
Provides: server-manager-images
Conflicts: ServiceLink-support
Obsoletes: e-smith-blades
Obsoletes: e-smith-keys
Obsoletes: e-smith-support
AutoReqProv: no

# remove old kernels that prevent upgrades
Obsoletes: kernel < 2.6.17
Obsoletes: kernel-smp < 2.6.17
Obsoletes: kernel-xenU < 2.6.17

# Kernel modules now included in kernel
Obsoletes: kmod-slip
Obsoletes: kmod-slip-smp
Obsoletes: kmod-slip-xenU

# remove old kernel modules that prevent upgrades 
Obsoletes: kernel-module-appletalk
Obsoletes: kernel-smp-module-appletalk

# Old dependencies from outdated atrpms/rpmforge packages
Obsoletes: libghttp
Obsoletes: perl-HTTP-GHTTP
Obsoletes: perl-Net_SSLeay.pm
Obsoletes: pythonabi

# Remove packages no longer needed or provided in COS5
Obsoletes: comps
Obsoletes: fonts-xorg-base
Obsoletes: pine
Obsoletes: system-config-keyboard
Obsoletes: system-config-mouse
Obsoletes: VFlib2
Obsoletes: xorg-x11-Mesa-libGL

# remove netatalk and modules
Obsoletes: e-smith-netatalk
Obsoletes: kmod-appletalk
Obsoletes: kmod-appletalk-smp
Obsoletes: kmod-appletalk-xenU
Obsoletes: netatalk

# SF: 1357548
Conflicts: selinux-policy-targeted

# XXX - FIXME - pam should require this, shouldn't it?
Requires: audit-libs

# New features that we want to pull in on upgrades
Requires: smolt
Requires: screen
Requires: smeserver-yum
Obsoletes: yum = 1.0.3-6.0.7.x.esmith
Requires: smeserver-clamav
Requires: e-smith-spamassassin
Requires: smeserver-audittools
Requires: e-smith-formmagick >= 1.4.0-9

# These packages weren't in 5.x, or were split from e-smith-base since then
Requires: e-smith-domains
Requires: e-smith-ibays
Requires: e-smith-nutUPS
Requires: e-smith-portforwarding
Requires: e-smith-starterwebsite

# 5.x used bind for name resolution - we need to pull in djbdns
Requires: e-smith-dnscache
Requires: e-smith-tinydns

# This one should probably be in e-smith-base
Obsoletes: kernel-module-slip
Obsoletes: kernel-smp-module-slip
Obsoletes: kernel-module-st

# Specific package versions we dont want.
# These aren't being pulled by anything else.
Obsoletes: e-smith-loginscript = 0.2-2
Obsoletes: e-smith-samba = 2.1.0-10gjz
Requires: e-smith-samba

# Pull in locales so we have a smooth language upgrade [SF: 1309520]
Requires: smeserver-locale-bg
Requires: smeserver-locale-da
Requires: smeserver-locale-de
Requires: smeserver-locale-el
Requires: smeserver-locale-es
Requires: smeserver-locale-et
Requires: smeserver-locale-fr
Requires: smeserver-locale-he
Requires: smeserver-locale-hu
Requires: smeserver-locale-id
Requires: smeserver-locale-it
Requires: smeserver-locale-ja
Requires: smeserver-locale-nb
Requires: smeserver-locale-nl
Requires: smeserver-locale-pl
Requires: smeserver-locale-pt
Requires: smeserver-locale-pt_BR
Requires: smeserver-locale-ro
Requires: smeserver-locale-ru
Requires: smeserver-locale-sl
Requires: smeserver-locale-sv
Requires: smeserver-locale-th
Requires: smeserver-locale-tr
Requires: smeserver-locale-zh_CN
Requires: smeserver-locale-zh_TW

# These should be re-pulled by other e-smith packages.
Obsoletes: perl-File-MMagic = 1.22-1
Obsoletes: perl-gettext = 1.01-10
Obsoletes: perl-perl-ldap = 0.22-10
Obsoletes: perl-perl-ldap = 0.31-1
Obsoletes: php = 4.3.10-01es01
Obsoletes: php-imap = 4.3.10-01es01
Obsoletes: php-ldap = 4.3.10-01es01
Obsoletes: php-mysql = 4.3.10-01es01
Obsoletes: proftpd = 4:1.2.5-fr1
Obsoletes: proftpd = 5:1.2.8p-es1
Obsoletes: proftpd = 5:1.2.9-es1
Obsoletes: proftpd = 5:1.2.9-es3
Obsoletes: proftpd = 5:1.2.9-es3sme1
Obsoletes: proftpd = 5:1.2.9-es4
Obsoletes: squid = 9:2.5.STABLE3-6.3E.2es01

# Specific package versions we dont want.
# These were installed with older version but aren't needed.
Obsoletes: authconfig = 4.2.8-4
Obsoletes: bind-utils = 9.2.1-1.7x.2
Obsoletes: cvs = 1.11.1p1-7es02
Obsoletes: cvs = 1.11.1p1-16.legacy.2
Obsoletes: cvs = 1.11.1p1-17.legacy.2
Obsoletes: dietlibc = 0.15-2
Obsoletes: e-smith-telnet = 1.6.0-02
Obsoletes: e-smith-reinstall-floppy <= 1.12.0-01
Obsoletes: gd = 1.8.4-4
Obsoletes: gd = 1.8.4-4.1.legacy
Obsoletes: logwatch = 5.2.2-1sme01
Obsoletes: mysqlclient9 = 3.23.22-8
Obsoletes: mysql-devel = 3.23.56-1.73
Obsoletes: mysql-devel = 3.23.58-1.73
Obsoletes: openldap-clients = 2.0.27-2.7.3es
Obsoletes: perl-Crypt-SSLeay = 0.35-15
Obsoletes: perl-Digest-Nilsimsa = 0.06-1
Obsoletes: perl-Filter-Handle = 0.03-10
Obsoletes: perl-I18N-LangTags = 0.27-1es3
Obsoletes: perl-NDBM_File = 1:1.75-34.99.6
Obsoletes: perl-Net-Ping = 2.28-1
Obsoletes: perl-Proc-PID_File = 0.05-1
Obsoletes: perl-Test-Harness-Straps = 0.10-1
Obsoletes: perl-Test-Simple = 0.42-1
Obsoletes: perl-Text-Wrapper = 1.000-10
Obsoletes: ppp-modules
Obsoletes: rpm-build = 4.0.4-7x.18
Obsoletes: sortspam = 1.0.0-01
Obsoletes: sortspam = 1.1.0-05
Obsoletes: sortspam = 1.1.0-05sme01
Obsoletes: sortspam = 1.1.0-05sme02
Obsoletes: telnet-server = 0.17-20
Obsoletes: e-smith-userpanel
Conflicts: e-smith-userpanel
Obsoletes: dmc-mitel-mailrules
Conflicts: dmc-mitel-mailrules

Obsoletes: php5-cgi
Conflicts: php5-cgi
Obsoletes: php5-cgi-imap
Conflicts: php5-cgi-imap
Obsoletes: php5-cgi-ldap
Conflicts: php5-cgi-ldap
Obsoletes: php5-cgi-mysql
Conflicts: php5-cgi-mysql
Obsoletes: php5-cgi-pear
Conflicts: php5-cgi-pear
Obsoletes: php5-cgi-xmlrpc
Conflicts: php5-cgi-xmlrpc

# This block used to be in the SMEServer RPM. Many are probably 
# redundant or should be elsewhere or removed
# [SF: 1356225]
Conflicts: amavis-ng
Conflicts: clamav-es
Obsoletes: obtuse-smtpd obtuse-smtpd-qmail
Obsoletes: ip_masq_h323 ip_masq_icq ip_masq_rtsp isapnptools
Obsoletes: pidentd
Obsoletes: tftp-conntrack-nat
Obsoletes: e-smith-named
Obsoletes: e-smith-locale-fr_CA
Obsoletes: pptp-conntrack-nat
Obsoletes: amavis-ng
Obsoletes: clamav-es
Requires: attr
Requires: audit
Requires: dos2unix
Requires: unix2dos
Requires: dstat
Requires: dvd+rw-tools
Requires: elinks
Requires: htop
Requires: mkisofs
Requires: mtr
Requires: nano
Requires: nc
Requires: mc
Requires: prelink
Requires: psacct
Requires: dmraid

# Dungog contribs which Stephen Noble reports as incompatible with
# SME 7.x [SME 1283] [SME 1295] [SME 2427]
Obsoletes: dungog-vdomain
Obsoletes: smeserver-vdomain
Conflicts: dungog-vdomain
Conflicts: smeserver-vdomain
Obsoletes: smeserver-userpanel <= 0.9-9
Obsoletes: dungog-autofs
Obsoletes: dungog-nis
Obsoletes: dungog-cgiinhtml
Obsoletes: dungog-ispconnection
Obsoletes: dungog-dialup
Obsoletes: dungog-masq
Obsoletes: dungog-sshd
Obsoletes: dungog-tmda
Obsoletes: dungog-ssl
Obsoletes: dungog-deletedoublebounce
Obsoletes: dungog-mailblocking
Conflicts: dungog-autofs
Conflicts: dungog-nis
Conflicts: dungog-cgiinhtml
Conflicts: dungog-ispconnection
Conflicts: dungog-dialup
Conflicts: dungog-masq
Conflicts: dungog-sshd
Conflicts: dungog-tmda
Conflicts: dungog-ssl
Conflicts: dungog-deletedoublebounce
Conflicts: dungog-mailblocking

# Remove rkhunter
Obsoletes: rkhunter <= 1.3.4-7.el5.sme

%changelog
* Tue Jul 13 2010 Shad L. Lords <slords@mail.com> - 2.2.0-18.sme
- Add support for Chinese (Taiwan) (zh_TW). [SME: 6106]

* Tue Jun 29 2010 Charlie Brady <charlieb@budge.apana.org.au> 2.2.0-17.sme
- Add Obsoletes for php5-cgi-{imap,ldap,mysql,pear,xmlrpc}. [SME: 6089]

* Mon Jun 28 2010 Charlie Brady <charlieb@budge.apana.org.au> 2.2.0-16.sme
- Add Obsoletes for php5-cgi. [SME: 6089]

* Tue May 25 2010 Shad L. Lords <slords@mail.com> - 2.2.0-15.sme
- Add support for Hebrew (he). [SME: 5971]

* Mon May 17 2010 Shad L. Lords <slords@mail.com> 2.2.0-14.sme
- Add migrate fragment for centos excludes [SME: 5960]

* Mon May 17 2010 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-13.sme
- Reverting previous change [SME: 5962]

* Mon May 17 2010 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-12.sme
- Migrate CentOS Exclude property default values to smeserver-yum [SME: 5962]

* Wed Dec  9 2009 Charlie Brady <charlieb@budge.apana.org.au> 2.2.0-11.sme
- Fix css validation errors. [SME: 5656]

* Tue Oct 27 2009 Shad L. Lords <slords@mail.com> 2.2.0-10.sme
- Add support for Polish (pl). [SME: 5434]
- Add support for Thai (th). [SME: 5466]

* Mon Oct 26 2009 Shad L. Lords <slords@mail.com> 2.2.0-9.sme
- obsoletes fonts-xorg-base to prevent dragging in unneeded
  packages [SME: 5535]

* Mon Oct 26 2009 Shad L. Lords <slords@mail.com> 2.2.0-8.sme
- add VFlib2 to obsoletes list so upgrades work [SME: 5532]

* Mon Aug 03 2009 Gavin Weight <gweight@gmail.com> 2.2.0-7.sme
- Add Obsoletes for kernel modules. [SME: 5386]

* Wed May 27 2009 Shad L. Lords <slords@mail.com> 2.2.0-6.sme
- Add support for Romanian (ro). [SME: 5268]

* Wed May 13 2009 Filippo Carletti <filippo.carletti@gmail.com> 2.2.0-5
- Obsoletes: rkhunter to remove from default install [SME: 5172]

* Wed Apr 29 2009 Gavin Weight <gweight@gmail.com> 2.2.0-4.sme
- Add support for Estonian (et). [SME: 5203]

* Tue Mar 3 2009 Shad L. Lords <slords@mail.com> 2.2.0-3.sme
- Add support for Norwegian Bokmal (nb) [SME: 5002 ]
- Add support for Russian (ru) [SME: 5002]
- Add support for Chinese China (zh_CN) [SME: 5002]

* Mon Oct 13 2008 Shad L. Lords <slords@mail.com> 2.2.0-2.sme
- Add support for Japanese (ja) [SME: 4637]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 1.6.0-53
- Update excludes for sme8 [SME: 4507]

* Thu Aug  7 2008 Charlie Brady <charlieb@e-smith.com> 1.6.0-52
- Remove incorrect 'Obsoletes: yum-metadata-parser'. [SME: 4466]

* Sat Jul 26 2008 Shad L. Lords <slords@mail.com> 1.6.0-51
- Add support for Bulgarian (bg) [SME: 4337]
- Re-add support for Portuguese (pt) [SME: 4006]
- Add support for Turkish (tr) [SME: 4443]

* Tue Mar 18 2008 Shad L. Lords <slords@mail.com> 1.6.0-50
- Add gettext to console titles.

* Tue Mar 18 2008 Shad L. Lords <slords@mail.com> 1.6.0-49
- Fix support for Portuguese (pt_BR) [SME: 4006]

* Wed Mar 12 2008 Shad L. Lords <slords@mail.com> 1.6.0-48
- Add support for Hungarian (hu) [SME: 4025]

* Sat Mar 07 2008 Stephen Noble <support@dungog.net> 1.6.0-47
- gettext Internet connection failed [SME: 631]

* Sat Mar 1 2008 Shad L. Lords <slords@mail.com> 1.6.0-46
- Add support for Danish (da) [SME: 4006]
- Add support for Dutch (nl) [SME: 4006]
- Add support for Greek (el) [SME: 4006]
- Add support for Indonesian (id) [SME: 4006]
- Add support for Portuguese (pt) [SME: 4006]
- Add support for Slovenian (sl) [SME: 4006]

* Wed Feb 13 2008 Stephen Noble <support@dungog.net> 1.6.0-45
- Remove <base> tags now in general [SME: 3928]

* Sat Feb 09 2008 Stephen Noble <support@dungog.net> 1.6.0-44
- move support lexicon  [SME: 3878]

* Fri Jan 11 2008 Shad L. Lords <slords@mail.com> 1.6.0-43
- Revert obsoletes check4updates, should be in smeserver-yum [SME: 3250]

* Fri Jan 11 2008 Stephen Noble <support@dungog.net> 1.6.0-42
- Add Obsolete check4updates   [SME: 3250]

* Mon Jan 7 2008 Gavin Weight <gweight@gmail.com> 1.6.0-41
- Remove check4updates requires line. [SME: 3250]

* Fri Sep 7 2007 Shad L. Lords <slords@mail.com> 1.6.0-40
- Update obsoletes for sme8 [SME: 2437]

* Tue Jul 3 2007 Shad L. Lords <slords@mail.com> 1.6.0-39
- Remove yum-metadata-parser under sme8.

* Wed Jun 6 2007 Shad L. Lords <slords@mail.com> 1.6.0-38
- Add smolt service for hardware profiling.

* Wed May 9 2007 Shad L. Lords <slords@mail.com> 1.6.0-37
- Updates to support SME Server 8

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com> 1.6.0-36
- Change to dist for tagging release
- Remove ipp2p support. [SME: 38]

* Mon Apr 09 2007 Stephen Noble <support@dungog.net> 1.6.0-35
- Add Obsoletes and Conflicts for old dungog contribs [SME: 1295]

* Sun Feb 18 2007 Shad L. Lords <slords@mail.com> 1.6.0-34
- Add sv locale so language files get pulled in [SME: 911]

* Sun Feb 18 2007 Shad L. Lords <slords@mail.com> 1.6.0-33
- Add ipp2p package (disabled) to block p2p traffic [SME: 38]

* Mon Feb 12 2007 Stephen Noble <support@dungog.net> 1.6.0-32
- Add Obsoletes header to remove smeserver-userpanel <=0.9-9 [SME: 2427]

* Sat Jan 27 2007 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-31
- Change base and updates Exclude definitions to defaults files [SME: 2384]

* Sat Jan 27 2007 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-30
- Fix generation of base and updates Exclude definitions [SME: 2384]

* Fri Jan 05 2007 Shad L. Lords <slords@mail.com> 1.6.0-29
- Add requires for check4updates.  It was split from atrpms.

* Tue Dec 12 2006 Shad L. Lords <slords@mail.com> 1.6.0-28
- Undo ntp obsoletes.  Breaks yum upgrades.

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Sat Dec 02 2006 Shad L. Lords <slords@mail.com> 1.6.0-27
- Obsolete our version of ntp so we pull correct upstream version

* Sat Dec 02 2006 Shad L. Lords <slords@mail.com> 1.6.0-26
- Update requires to reflect new kernel module format

* Wed Nov 22 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-25
- Remove requires for smeserver-qpsmtpds-tnef2mime after merge [SME: 2087]

* Sat Nov 18 2006 Shad L. Lords <slords@mail.com> 1.6.0-24
- Remove CentOS markings from motd, redhat-release to fix
  branding of kernels in grub.conf and startup screens [SME: 1996]

* Tue Nov 14 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-23
- Revert last change - the packages can be removed manually [SME: 2062]

* Tue Nov 14 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-22
- Obsolete samba-3.0.23c-1 and friends [SME: 2062]

* Fri Sep 8 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-21
- Add centos_exclude define and use it to auto-generate Exclude 
  property for CentOS yum repositories [SME: 1849]

* Sun Jul 16 2006 Gavin Weight <gweight@gmail.com> 1.6.0-20
- Changed css style to match logo background. [SME: 1558]

* Fri Jun 30 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-19
- Change donate link to www.smeserver.org/donate/ [SME: 1668]

* Fri Jun 30 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-18
- Change new window target to _blank rather than "new" [SME: 1613]

* Thu Jun 29 2006 Gavin Weight <gweight@gmail.com> 1.6.0-17
- Modified text on server-manager front screen. [SME: 1613]

* Wed Jun 28 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-16
- Expand text on server-manager front screen [SME: 1613]
- Add Copyright 2006 SME Server, Inc to footer

* Fri Jun 9 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-15
- Add GIF format logo [SME: 1558]

* Thu Jun 8 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-14
- Update server-manager logo [SME: 1558]

* Wed May 31 2006 Charlie Brady <charlie_brady@mitel.com> 1.6.0-13
- Escape percent char in crontab template. [SME: 1497]

* Wed May 31 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-12
- Obsolete yum-1.0.3-6.0.7.x.esmith [SME: 1418]

* Wed May 31 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-11
- Updated SME Server logo [SME: 1512]

* Fri May 26 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-10
- Sleep 0..59 seconds when calling statusreport from cron [SME: 1497]

* Tue May 23 2006 Gavin Weight <gweight@gmail.com> 1.6.0-09
- Add Obsoletes for perl-File-MMagic. [SME: 1436]

* Thu May 23 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-08
- Don't bother printing LWP error [SME: 1314]

* Thu May 23 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-07
- Add weekly status report. 
- Only the following information is passed in the status report:
  - ReleaseVersion (e.g. 7.0rc2)
  - SystemMode     (e.g. servergateway)
  - SystemIDHash   (Unique id - SHA1 hash of the SystemID)
  - InstallEpoch   (time of system install)
  - CurrentEpoch   (time of this test)
- Refactor testInternet to use new script
- [SME: 1314]

* Wed Apr 19 2006 Charlie Brady <charlie_brady@mitel.com> 1.6.0-06
- Add Obsoletes and Conflicts headers for dungog vdomain contribs.
  [SME: 1283]

* Thu Apr 6 2006 Gavin Weight <gweight@gmail.com> 1.6.0-05
- Changed links to online-manual now at contribs.org . [SME: 1079]

* Wed Apr 5 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-04
- Add dependency on smeserver-audittools [SME: 762]

* Tue Mar 28 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-03
- Bump CentOS release to 4.3 [SME: 1151]

* Tue Mar 28 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-02
- Add Obsoletes for e-smith-loginscript-0.2-2 [SME: 1087]

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.6.0-01
- Roll stable stream version. [SME: 1016]

* Wed Feb 22 2006 Gavin Weight <gweight@gmail.com> 1.4.8-22
- Add obsoletes on amavis-ng and clamav-es, Added conflicts too [SME: 775]

* Mon Feb 20 2006 Gordon Rowell <gordonr@gormand.com.au> 1.4.8-21
- And e-smith-portforwarding [SME: 767]

* Mon Feb 20 2006 Gordon Rowell <gordonr@gormand.com.au> 1.4.8-20
- Add dependencies on e-smith-domains, e-smith-nutUPS and
  e-smith-starterwebsite to simplify 5.x upgrades [SME: 767]
- Obsolete a few more old versions of proftpd with big Epoch tags [SME: 767]

* Wed Feb 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.4.8-19
- Add Obsoletes and Conflicts headers to cause removal of and
  prevent re-installation of the incompatible contrib
  dmc-mitel-mailrules. [SME: 800]

* Tue Feb 14 2006 Charlie Brady <charlie_brady@mitel.com> 1.4.8-18
- Add Conflicts header to prevent reinstallation of e-smith-userpanel.
  [SME: 598,770]

* Mon Feb 13 2006 Charlie Brady <charlieb@e-smith.com> 1.4.8-17
- Add more Obsoletes headers, to assist with upgrade of customised
  servers. [SME: 775]

* Mon Feb 13 2006 Charlie Brady <charlieb@e-smith.com> 1.4.8-16
- Adding dependencies on e-smith-dnscache and e-smith-tinydns, so
  that DNS works after 5.x -> 7 upgrade. [SME: 767]

* Sun Feb 12 2006 Charlie Brady <charlieb@e-smith.com> 1.4.8-15
- Adding dependency on e-smith-ibays, to ensure it is installed
  during 5.x -> 7 upgrade. [SME: 747]

* Fri Feb 10 2006 Gavin Weight <gweight@gmail.com> 1.4.8-14
- Updated online-manual to include links to Sourceforge
  Manual/FAQs/KnownIssues. [SME: 490]

* Thu Feb 9 2006 Gavin Weight <gweight@gmail.com> 1.4.8-13
- Added online-manual. [SME: 407]

* Wed Feb 8 2006 Gavin Weight <gweight@gmail.com> 1.4.8-12
- Additional cleanup of sme_header.css [SME: 408]

* Wed Feb 8 2006 Gordon Rowell <gordonr@gormand.com.au> 1.4.8-11
- Additional cleanup of contribs.org styling by Gavin [SME: 408]

* Tue Feb 7 2006 Gordon Rowell <gordonr@gormand.com.au> 1.4.8-10
- Add comment to each of the contribs.org styling fragments
  so it is easier to find the overrides [SME: 408]

* Tue Feb 7 2006 Gavin Weight <gweight@gmail.com> 1.4.8-09
- Adding contribs css style fragments and removing hack in
  contribs.org styling [SME: 408]

* Sun Feb 05 2006 Gavin Weight <gweight@gmail.com> 1.4.8-08
- Add header to obsolete kernel-module-st. [SME: 647]

* Sat Feb 4 2006 Gordon Rowell <gordonr@gormand.com.au> 1.4.8-07
- Hack in contribs.org styling for CSS files prior to parameterizing
  the templates. Kids: Don't do this at home. RPMs should NOT install
  fragments into templates-custom. [SME: 408]

* Wed Feb 01 2006 Charlie Brady <charlie_brady@mitel.com> 1.4.8-06
- Add header to obsolete e-smith-userpanel. [SME: 598]

* Mon Jan 30 2006 Charlie Brady <charlie_brady@mitel.com> 1.4.8-05
- Add dependencies for spamassassin and clamav frameworks (moved
  from smeserver-qpsmtpd). [SME: 606]

* Thu Jan 12 2006 Gordon Rowell <gordonr@gormand.com.au> 1.4.8-04
- Add screen package [SME: 445]

* Thu Jan 5 2006 Gordon Rowell <gordonr@gormand.com.au> 1.4.8-03
- Adjust initial.cgi to "SME Server" product name [SME: 402]

* Thu Jan 5 2006 Gordon Rowell <gordonr@gormand.com.au> 1.4.8-02
- Add contribs.org logo and change product name to "SME Server" [SME: 402]
- Put $SystemName.$DomainName in manager titlebar

* Thu Jan 5 2006 Gordon Rowell <gordonr@gormand.com.au> 1.4.8-01
- Roll patches to 1.4.7-24 and convert some stray DOS format text files
  to Unix format

* Thu Jan 5 2006 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-24
- Modify "Test Internet Access" so that it accesses contribs.org
  and only passes two pieces of information:
  - sysconfig{ReleaseVersion}
  - An SHA1 hash of sysconfig{SystemID} [SME: 402]

* Sat Dec 25 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-23
- Add esmith::console object for standalone menu item [SME: 364]

* Sat Dec 25 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-22
- Move testInternet console menu item to smeserver-support [SME: 364]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-21
- Revert last change [SME: 327]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-20
- Add Requires: smeserver-sysstat [SME: 327]

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-19
- Relocate Obsoletes: SMEServer to smeserver-release package [SME: 72]

* Fri Nov 18 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-18
- Expand /etc/motd and friends in post-{install,upgrade} so that
  they are correct for the first boot [SF: 1295403, 1261360]

* Fri Nov 18 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-17
- Obsolete the SMEServer marker package [SF: 1356225]

* Fri Nov 18 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-16
- /etc/issue and /etc/issue.net should be empty by default. We don't
  want to announce version numbers to casual observers [SF: 1261360]

* Fri Nov 18 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-15
- Use the /etc/motd template for /etc/redhat-release [SF: 1295403]

* Wed Nov 16 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-14
- Add templates for /etc/{issue,issue.net,motd}, all generated from
  the /etc/motd template [SF: 1261360]

* Wed Nov 16 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-13
- Add Conflicts: selinux-policy-targeted [SF: 1357548]

* Mon Nov 14 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-12
- Add requires for kernel-smp-module-slip [SF: 1356104]

* Mon Nov 14 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-11
- Removed Requires for php-domxml - now in e-smith-horde [SF: 1313299]

* Mon Oct 31 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-10
- Obsolete e-smith-reinstall-floppy [SF: 1342860]

* Sat Oct 25 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-09
- Add dependency on audit-libs

* Fri Oct 24 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-08
- Remove kenel-module-st - patch is in the CentOS 4.2 kernel

* Mon Oct 17 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-07
- Make symlink to tux in post scriptlet [SF: 1295038]

* Mon Oct 17 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-06
- Add symlink to tux for splash.xpm.gz [SF: 1295038]
- Remove unused language macro definition from SPEC file

* Sat Oct 15 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-05
- And add dependencies for smeserver-locale-{de,es,fr,it} [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-04
- Move all L10Ns to smeserver-locale [SF: 1309520]

* Mon Oct 10 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-03
- Bump version to force update

* Fri Oct 7 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-02
- Pull in kernel-module-st so flexbackup works [SF: 1254300]
- Pull in kernel-module-slip for dialup support [SF: 1293606]

* Fri Oct 7 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.7-01
- Roll tarball, patches to 1.4.6-02

* Mon Sep 26 2005 Gordon Rowell <gordonr@gormand.com.au> 1.4.6-02
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Mon Sep 26 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.4.6-01]
- Roll patches up to 1.4.5-07
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Thu Aug 18 2005 Shad L. Lords <slords@mail.com>
- [1.4.5-07]
- More Obsoletes/Requires updates

* Thu Aug 18 2005 Shad L. Lords <slords@mail.com>
- [1.4.5-06]
- Obsoletes/Requires updates for beta1.
  Still lots of work to be done.

* Sat Aug 13 2005 Shad L. Lords <slords@mail.com>
- [1.4.5-05]
- Lots up Obsoletes updates

* Fri Aug 12 2005 Shad L. Lords <slords@mail.com>
- [1.4.5-04]
- Add authconfig, mysql-devel, openldap-clients,
  perl-Crypt-SSLeay, perl-NDBM_File specific and  
  ppp-modules generic obsoletes so they are removed 
  on upgrade.

* Fri Aug 12 2005 Shad L. Lords <slords@mail.com>
- [1.4.5-03]
- Add obsoletes for specific php versions

* Tue Aug 09 2005 Shad L. Lords <slords@mail.com>
- [1.4.5-02]
- Remove Requires and Obsoletes.  Start moving to correct places.

* Mon Jul 18 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.4.5-01]
- Package renamed to smeserver-support, obsoleting e-smith-support

* Fri Jul 15 2005 Shad L. Lords <slords@mail.com>
- [1.4.4-07sme02]
- Various additional fixes for upgrades

* Thu Jul 14 2005 Shad L. Lords <slords@mail.com>
- [1.4.4-07sme01]
- Various fixes for 6.5RC1 upgrades

* Fri Jul 1 2005 Gordon Rowell <gordonr@gormand.com.au>
* Thu Jul 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.4.4-07]
- Various updates provided by Shad Lords.

* Fri Jul 1 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.4.4-06]
- Updated Requires lists for CentOS 4.1 version [SF: 1217914]

* Wed Jun 15 2005 Charlie Brady <charlieb@e-smith.com>
- [1.4.4-05]
- Add full set of Requires: headers, to ensure that an upgrade installs
  a full package set. [SF: 1217914]

* Tue Jun  7 2005 Charlie Brady <charlieb@e-smith.com>
- [1.4.4-04]
- Rationalise manager URLs below server-manager. [SF: 1172203, 1210715]

* Mon May 30 2005 Charlie Brady <charlieb@e-smith.com>
- [1.4.4-03]
- Add "Requires: e-smith-lib" to ensure correct installation ordering.
  [SF: 1210723]

* Thu Feb 24 2005 Charlie Brady <charlieb@e-smith.com>
- [1.4.4-02]
- Updated copyright date on the license text file.

* Thu Jun 12 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.4.4-01]
- Updated product_logo.jpg [gordonr 8507]

* Mon May 12 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.4.3-01]
- Handle "es" language (treat as English) [gordonr 3793]

* Mon Mar 31 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.4.2-08]
- Updated fr lexicon for initial.cgi [gordonr 7728]

* Fri Mar 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.4.2-07]
- Moved lexica for {index,initial}.cgi here [gordonr 7728]

* Fri Mar 28 2003 Lijie Deng <lijied@e-smith.com>
- [1.4.2-06]
- Modified French lexicon to use lang="fr", rename the lexicon
  directory to fr [lijied 6787] 

* Tue Mar 25 2003 Mark Knox <markk@e-smith.com>
- [1.4.2-05]
- Renamed 20FooterText to 20ProductName, factored out common text [markk 7715]

* Mon Mar 17 2003 Mark Knox <markk@e-smith.com>
- [1.4.2-04]
- Added header template [markk 4722]
- Added footer template [markk 7714]

* Thu Mar 13 2003 Mark Knox <markk@e-smith.com>
- [1.4.2-03]
- Corrected header image size in 40LogoRow [markk 4722]

* Thu Mar 13 2003 Mark Knox <markk@e-smith.com>
- [1.4.2-02]
- Added 40LogoRow header fragment with correct ALT text and image [markk 4722]

* Thu Mar 13 2003 Mark Knox <markk@e-smith.com>
- [1.4.2-01]
- Added new product_logo.jpg [markk 4722]

* Fri Jan 10 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.4.1-04]
- New URL for www.e-smith.com [gordonr 6227]

* Fri Jan 10 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.4.1-03]
- Adjusted header on license text
  Create fr_CA license on the fly [gordonr 6227]

* Mon Dec 30 2002 Charlie Brady <charlieb@e-smith.com>
- [1.4.1-02]
- Add Obsoletes header to force removal of e-smith-keys. [charlieb 6369]

* Fri Dec 27 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.4.1-01]
- Updated banner image [gordonr 6227]

* Tue Dec 24 2002 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Roll stable version to 1.4.0

* Tue Dec 24 2002 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01-01]
- Roll stable version to 1.4.0-01

* Tue Dec 24 2002 Charlie Brady <charlieb@e-smith.com>
- [1.3.12-02]
- Add Obsoletes head to force removal of e-smith-blades. [charlieb 5416]

* Fri May 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.12-01]
- Place lexicon in target directory. Re-add original support CGI script
  [gordonr 3641]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.11-01]
- RPM rebuild forced by cvsroot2rpm

* Tue May 21 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.10-01]
- Move French localisation for support panel here [gordonr 3582]

* Thu May 16 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.9-01]
- Relocated license text for locale awareness [gordonr 3413]

* Wed May 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.8-01]
- Missing U.S. English nav bar entry [gordonr 3421]

* Wed May  8 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.7-01]
- Added footer [gordonr 3223]

* Wed May  8 2002 Mark Knox <markk@e-smith.com>
- [1.3.6-01]
- Quickly i18n'd into FormMagick panel. [markk 3309]

* Fri Apr 19 2002 Mark Knox <markk@e-smith.com>
- [1.3.5-01]
- Updated server-manager image [markk 3188]

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.4-01]
- Removed copy of %Source1 - now in correct place/name

* Thu Apr 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.3-01]
- Removed airiness from licence [gordonr 3119]

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.2-01]
- Re-did createlinks

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.1-01]
- Initial build from CVS

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-01]
- rollRPM: Rolled version number to 1.3.0-01. Includes patches up to 1.2.0-02.

* Mon Jan 07 2002 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-02]
- Add conflicts header to prevent ServiceLink-support and e-smith-support from
  being installed simultaneously.

* Tue Dec 11 2001 Jason Miller <jay@e-smith.com>
- [1.2.0-01]
- rollRPM: Rolled version number to 1.2.0-01. Includes patches up to 1.1.0-06.

* Wed Nov 21 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-06]
- Remove e-smith-lib dependency as well - e-smith-lib requires e-smith-support,
  but not vice-versa.

* Wed Nov 21 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-05]
- Remove troublesome e-smith-base dependency, which isn't real anyway.
- While we are at it, remove the e-smith => 4 dependency - not really relevant
  and forces us to retain the empty e-smith RPM.

* Wed Nov 14 2001 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-04]
- s/March/Mitel/ in license text

* Thu Nov 08 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-03]
- Updated with (YA) new banner image

* Fri Nov 2 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-02]
- Updated with new banner image

* Fri Nov 2 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-01]
- Rolled version number to 1.1.0-01. Includes patches upto 1.0.0-03.

* Tue Aug 21 2001 Charlie Brady <charlieb@e-smith.com>
- [1.0.0-03]
- Removed pre-1.0.0 changelog entries.

* Tue Aug 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.0.0-02]
- Changed Copyright to GPL and added Vendor tag

* Tue Aug 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.0.0-01]
- Rolled version number to 1.0.0-01. Includes patches upto 0.1.1-24.

%description
SME Server module to display support and licensing information

%prep
%setup
%patch0 -p1
%patch1 -p1
cp %{SOURCE1} root/etc/e-smith/web/common
cp %{SOURCE2} root/etc/e-smith/web/common

%build
perl createlinks

ln -s initial.cgi root/etc/e-smith/locale/en-us/etc/e-smith/web/functions/index.cgi

YUM_REPOS=root/etc/e-smith/db/yum_repositories/
for dir in base updates
do
    mkdir -p $YUM_REPOS/defaults/$dir
    echo %{centos_excludes} > $YUM_REPOS/defaults/$dir/Exclude
done
sed -i 's/CENTOS_EXCLUDES/%{centos_excludes}/' $YUM_REPOS/migrate/25CentOSExcludes
sed -i 's/CENTOS_REMOVE/%{centos_remove}/' $YUM_REPOS/migrate/25CentOSExcludes

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -f /boot/grub/splash.xpm.gz ] || ln -s tux.xpm.gz /boot/grub/splash.xpm.gz
/bin/true

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
