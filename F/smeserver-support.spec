Summary: SME Server module to display support and licensing information
%define name smeserver-support
Name: %{name}
%define version 1.4.7
%define release 20
Version: %{version}
Release: %{release}
License: GPL
Vendor: SME Server Developers
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: smeserver-support-1.4.7-motd.patch3
Patch1: smeserver-support-1.4.7-redhatrelease.patch
Patch2: smeserver-support-1.4.7-redhatrelease.patch2
Patch3: smeserver-support-1.4.7-blanketcissue.patch
Patch4: smeserver-support-1.4.7-events.patch
Packager: Gordon Rowell <gordonr@gormand.com.au>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools >= 1.7.5
BuildArchitectures: noarch
Provides: server-manager-images
Conflicts: ServiceLink-support
Obsoletes: e-smith-blades
Obsoletes: e-smith-keys
Obsoletes: e-smith-support
AutoReqProv: no

# SF: 1357548
Conflicts: selinux-policy-targeted

# XXX - FIXME - pam should require this, shouldn't it?
Requires: audit-libs

# New features that we want to pull in on upgrades
Requires: rkhunter
Requires: smeserver-yum
Requires: smeserver-sysstat

# This one should probably be in e-smith-base
Requires: kernel-module-slip
Requires: kernel-smp-module-slip

# Specific package versions we dont want.
# These aren't being pulled by anything else.
Obsoletes: e-smith-samba = 2.1.0-10gjz
Requires: e-smith-samba

# Pull in locales so we have a smooth language upgrade [SF: 1309520]
Requires: smeserver-locale-de
Requires: smeserver-locale-es
Requires: smeserver-locale-fr
Requires: smeserver-locale-it

# These should be re-pulled by other e-smith packages.
Obsoletes: perl-gettext = 1.01-10
Obsoletes: perl-perl-ldap = 0.22-10
Obsoletes: perl-perl-ldap = 0.31-1
Obsoletes: php = 4.3.10-01es01
Obsoletes: php-imap = 4.3.10-01es01
Obsoletes: php-ldap = 4.3.10-01es01
Obsoletes: php-mysql = 4.3.10-01es01
Obsoletes: proftpd = 5:1.2.9-es1
Obsoletes: proftpd = 5:1.2.9-es3
Obsoletes: proftpd = 5:1.2.9-es4
Obsoletes: squid = 9:2.5.STABLE3-6.3E.2es01

# Specific package versions we dont want.
# These were installed with older version but aren't needed.
Obsoletes: authconfig = 4.2.8-4
Obsoletes: bind-utils = 9.2.1-1.7x.2
Obsoletes: cvs = 1.11.1p1-7es02
Obsoletes: cvs = 1.11.1p1-16.legacy.2
Obsoletes: dietlibc = 0.15-2
Obsoletes: e-smith-telnet = 1.6.0-02
Obsoletes: e-smith-reinstall-floppy <= 1.12.0-01
Obsoletes: gd = 1.8.4-4
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
Obsoletes: sortspam = 1.1.0-05sme02
Obsoletes: telnet-server = 0.17-20

# This block used to be in the SMEServer RPM. Many are probably 
# redundant or should be elsewhere or removed
# [SF: 1356225]
Obsoletes: obtuse-smtpd obtuse-smtpd-qmail
Obsoletes: ip_masq_h323 ip_masq_icq ip_masq_rtsp isapnptools
Obsoletes: pidentd
Obsoletes: tftp-conntrack-nat
Obsoletes: e-smith-named
Obsoletes: e-smith-locale-fr_CA
Obsoletes: pptp-conntrack-nat
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

%changelog
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
%patch2 -p1
%patch3 -p1
%patch4 -p1

mkdir -p root/etc/e-smith/templates/etc/issue
touch root/etc/e-smith/templates/etc/issue/template-begin

rm -f root/etc/e-smith/web/common/e-smith-manager.gif
rm -rf root/etc/e-smith/locale/de
rm -rf root/etc/e-smith/locale/fr
rm -rf root/etc/e-smith/locale/es
rm -rf root/etc/e-smith/locale/it
rm -rf root/etc/e-smith/licenses/fr
rm -rf root/etc/e-smith/licenses/fr_CA

%build
perl createlinks

ln -s initial.cgi root/etc/e-smith/locale/en-us/etc/e-smith/web/functions/index.cgi

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
