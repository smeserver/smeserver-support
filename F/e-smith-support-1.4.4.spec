Summary: e-smith module to display support and licensing information
%define name e-smith-support
%define language fr_CA
Name: %{name}
%define version 1.4.4
%define release 06sme03
Version: %{version}
Release: %{release}
License: GPL
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-support-1.4.4-02.mitel_patch
Patch1: e-smith-support-1.4.4-04.mitel_patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools >= 1.7.5
BuildArchitectures: noarch
Provides: server-manager-images
Conflicts: ServiceLink-support
Obsoletes: e-smith-blades
Obsoletes: e-smith-keys
AutoReqProv: no

# BEGIN include requires.txt
Requires: acl
Requires: acpid
Requires: anacron
Requires: apmd
Requires: apr
Requires: apr-util
Requires: ash
Requires: aspell
Requires: aspell-ca
Requires: aspell-en
Requires: aspell-es
Requires: aspell-fr
Requires: at
Requires: attr
Requires: audit
Requires: authconfig
Requires: autofs
Requires: basesystem
Requires: bash
Requires: bc
Requires: beecrypt
Requires: bind-libs
Requires: bind-utils
Requires: binutils
Requires: bridge-utils
Requires: buffer
Requires: bzip2
Requires: bzip2-libs
Requires: cdrecord
Requires: centos-release
Requires: checkpassword
Requires: checkpolicy
Requires: chkconfig
Requires: clamav
Requires: clamav-db
Requires: clamd
Requires: comps
Requires: coreutils
Requires: cpio
Requires: cracklib
Requires: cracklib-dicts
Requires: crontabs
Requires: cryptsetup
Requires: cups
Requires: cups-libs
Requires: curl
Requires: cvm
Requires: cvs
Requires: cyrus-sasl
Requires: cyrus-sasl-md5
Requires: cyrus-sasl-plain
Requires: daemontools
Requires: db4
Requires: dbus
Requires: dbus-glib
Requires: DCC
Requires: desktop-file-utils
Requires: device-mapper
Requires: dhclient
Requires: dhcp
Requires: diald
Requires: diald-top
Requires: diffutils
Requires: distcache
Requires: djbdns
Requires: dmraid
Requires: dos2unix
Requires: dosfstools
Requires: dot-forward
Requires: dovecot
Requires: dstat
Requires: dump
Requires: dvd+rw-tools
Requires: e2fsprogs
Requires: ed
Requires: eject
Requires: elfutils
Requires: elfutils-libelf
Requires: elinks
Requires: e-smith
Requires: e-smith-apache
Requires: e-smith-apache-proxy
Requires: e-smith-backup
Requires: e-smith-base
Requires: e-smith-clamav
Requires: e-smith-cvm-unix-local
Requires: e-smith-devtools
Requires: e-smith-dnscache
Requires: e-smith-domains
Requires: e-smith-dynamicdns-dyndns
Requires: e-smith-dynamicdns-dyndns.org
Requires: e-smith-dynamicdns-tzo
Requires: e-smith-dynamicdns-yi
Requires: e-smith-email
Requires: e-smith-flexbackup
Requires: e-smith-formmagick
Requires: e-smith-grub
Requires: e-smith-horde
Requires: e-smith-hosts
Requires: e-smith-ibays
Requires: e-smith-imap
Requires: e-smith-imp
Requires: e-smith-ipmasq
Requires: e-smith-ldap
Requires: e-smith-lib
Requires: e-smith-lib-compspec
Requires: e-smith-lib-Tai64n
Requires: e-smith-LPRng
Requires: e-smith-manager
Requires: e-smith-mysql
Requires: e-smith-netatalk
Requires: e-smith-ntp
Requires: e-smith-nutUPS
Requires: e-smith-oidentd
Requires: e-smith-openssh
Requires: e-smith-packetfilter
Requires: e-smith-php
Requires: e-smith-portforwarding
Requires: e-smith-pptpd
Requires: e-smith-proftpd
Requires: e-smith-proxy
Requires: e-smith-qmailanalog
Requires: e-smith-qpsmtpd
Requires: e-smith-quota
Requires: e-smith-radiusd
Requires: e-smith-regedit
Requires: e-smith-release
Requires: e-smith-rpm
Requires: e-smith-runit
Requires: e-smith-samba
Requires: e-smith-spamassassin
Requires: e-smith-starterwebsite
Requires: e-smith-test
Requires: e-smith-tinydns
Requires: e-smith-turba
Requires: e-smith-viewlogfiles
Requires: ethtool
Requires: expat
Requires: fastforward
Requires: fbset
Requires: fetchmail
Requires: file
Requires: filesystem
Requires: findutils
Requires: finger
Requires: flexbackup
Requires: fontconfig
Requires: freeradius
Requires: freetype
Requires: ftp
Requires: gawk
Requires: gd
Requires: gdbm
Requires: gettext
Requires: glib
Requires: glib2
Requires: glibc
Requires: glibc-common
Requires: gmp
Requires: gnupg
Requires: gnutls
Requires: gpm
Requires: grep
Requires: groff
Requires: grub
Requires: gzip
Requires: hal
Requires: hdparm
Requires: hesiod
Requires: horde
Requires: hotplug
Requires: htmlview
Requires: htop
Requires: httpd
Requires: httpd-suexec
Requires: hwdata
Requires: imp-h3
Requires: indexhtml
Requires: info
Requires: initscripts
Requires: iproute
Requires: ipsec-tools
Requires: ipsvd
Requires: iptables
Requires: iptraf
Requires: iptstate
Requires: iputils
Requires: isdn4k-utils
Requires: jwhois
Requires: kbd
Requires: kernel
Requires: kernel-module-ppp-2.6.9-11.EL
Requires: kernel-smp
Requires: kernel-smp-module-ppp-2.6.9-11.EL
Requires: kernel-utils
Requires: krb5-libs
Requires: krb5-workstation
Requires: kudzu
Requires: less
Requires: lftp
Requires: lha
Requires: libacl
Requires: libattr
Requires: libcap
Requires: libc-client
Requires: libgcc
Requires: libgcrypt
Requires: libgpg-error
Requires: libidn
Requires: libjpeg
Requires: libpcap
Requires: libpng
Requires: libselinux
Requires: libsepol
Requires: libstdc++
Requires: libtermcap
Requires: libtiff
Requires: libtool-libs
Requires: libusb
Requires: libuser
Requires: libwvstreams
Requires: libxml2
Requires: libxml2-python
Requires: libxslt
Requires: lm_sensors
Requires: lockdev
Requires: logrotate
Requires: logwatch
Requires: LPRng
Requires: lrzsz
Requires: lsof
Requires: lvm2
Requires: lynx
Requires: m4
Requires: mailcap
Requires: mailfront
Requires: mailx
Requires: make
Requires: MAKEDEV
Requires: man
Requires: mbuffer
Requires: mdadm
Requires: mgetty
Requires: mingetty
Requires: minicom
Requires: mkbootdisk
Requires: mkinitrd
Requires: mkisofs
Requires: mktemp
Requires: mod_auth_external
Requires: mod_perl
Requires: mod_python
Requires: mod_ssl
Requires: module-init-tools
Requires: mtools
Requires: mtr
Requires: mt-st
Requires: mutt
Requires: mysql
Requires: mysql-server
Requires: nano
Requires: nc
Requires: ncurses
Requires: netatalk
Requires: netconfig
Requires: net-snmp
Requires: net-snmp-libs
Requires: net-snmp-perl
Requires: net-snmp-utils
Requires: net-tools
Requires: newt
Requires: newt-perl
Requires: nscd
Requires: nss_db
Requires: nss_ldap
Requires: ntp
Requires: nut
Requires: nut-client
Requires: oidentd
Requires: openldap
Requires: openldap-servers
Requires: openssh
Requires: openssh-clients
Requires: openssh-server
Requires: openssl
Requires: openssl-perl
Requires: pam
Requires: pam_ccreds
Requires: pam_krb5
Requires: pam_passwdqc
Requires: pam_smb
Requires: parted
Requires: passwd
Requires: patch
Requires: pax
Requires: pciutils
Requires: pcmcia-cs
Requires: pcre
Requires: pdksh
Requires: pear-date
Requires: pear-db
Requires: pear-file
Requires: pear-log
Requires: pear-mail
Requires: pear-mail_mime
Requires: perl
Requires: perl-Authen-PAM
Requires: perl-Authen-SASL
Requires: perl-Bit-Vector
Requires: perl-CGI-FormMagick
Requires: perl-CGI-Persistent
Requires: perl-Class-ParamParser
Requires: perl-Clone
Requires: perl-Convert-ASN1
Requires: perl-Convert-TNEF
Requires: perl-Crypt-Cracklib
Requires: perl-Date-Calc
Requires: perl-DateManip
Requires: perl-DBD-MySQL
Requires: perl-DBI
Requires: perl-Digest-HMAC
Requires: perl-Digest-SHA1
Requires: perl-Error
Requires: perl-File-MMagic
Requires: perl-Filter
Requires: perl-FreezeThaw
Requires: perl-HTML-Parser
Requires: perl-HTML-Tagset
Requires: perl-I18N-AcceptLanguage
Requires: perl-IO-stringy
Requires: perl-LDAP
Requires: perl-libwww-perl
Requires: perl-Locale-gettext
Requires: perl-Mail-RFC822-Address
Requires: perl-MIME-Tools
Requires: perl-Net-DNS
Requires: perl-Net-IPv4Addr
Requires: perl-Net-Server
Requires: perl-Object-Persistence
Requires: perl-Parse-Syslog
Requires: perl-Quota
Requires: perl-RPM2
Requires: perl-Statistics-Distributions
Requires: perl-suidperl
Requires: perl-Test-Inline
Requires: perl-Text-Iconv
Requires: perl-Text-Template
Requires: perl-TimeDate
Requires: perl-Time-HiRes
Requires: perl-Time-modules
Requires: perl-Unicode-String
Requires: perl-Unix-ConfigFile
Requires: perl-URI
Requires: perl-WWW-Automate
Requires: perl-XML-NamespaceSupport
Requires: perl-XML-Parser
Requires: perl-XML-SAX
Requires: php
Requires: php-domxml
Requires: php-gd
Requires: php-imap
Requires: php-ldap
Requires: php-mbstring
Requires: php-mysql
Requires: php-pear
Requires: php-xmlrpc
Requires: pinfo
Requires: policycoreutils
Requires: popt
Requires: postgresql-libs
Requires: ppp
Requires: pptpd
Requires: prelink
Requires: procmail
Requires: procps
Requires: proftpd
Requires: psacct
Requires: psmisc
Requires: pyOpenSSL
Requires: python
Requires: pyxf86config
Requires: pyzor
Requires: qmail
Requires: qmailanalog
Requires: qmail-qfilter
Requires: qpsmtpd
Requires: qpsmtpd-plugins-openfusion
Requires: quota
Requires: radiusclient
Requires: razor-agents
Requires: rcs
Requires: rdate
Requires: readline
Requires: redhat-lsb
Requires: redhat-menus
Requires: rhnlib
Requires: rhpl
Requires: rkhunter
Requires: rmt
Requires: rootfiles
Requires: rpm
Requires: rpm-build
Requires: rpmdb-CentOS
Requires: rpm-libs
Requires: rpm-python
Requires: rp-pppoe
Requires: rssh
Requires: rsync
Requires: runit
Requires: safecat
Requires: samba
Requires: samba-client
Requires: samba-common
Requires: schedutils
Requires: screen
Requires: sed
Requires: selinux-policy-targeted
Requires: setarch
Requires: setools
Requires: setserial
Requires: setup
Requires: setuptool
Requires: shadow-utils
Requires: slang
Requires: slocate
Requires: SMEServer
Requires: smeserver-qpsmtpd-tnef2mime
Requires: smeserver-yum
Requires: sortspam
Requires: spamassassin
Requires: specspo
Requires: squid
Requires: star
Requires: statserial
Requires: strace
Requires: stunnel
Requires: stunnel-tls
Requires: sudo
Requires: symlinks
Requires: sysfsutils
Requires: sysklogd
Requires: syslinux
Requires: sysreport
Requires: sysstat
Requires: SysVinit
Requires: tai64nunix
Requires: tar
Requires: tcpdump
Requires: tcp_wrappers
Requires: tcsh
Requires: telnet
Requires: termcap
Requires: time
Requires: tmpwatch
Requires: tnef
Requires: traceroute
Requires: turba-h3
Requires: tzdata
Requires: ucspi-tcp
Requires: udev
Requires: ulogd
Requires: unix2dos
Requires: unzip
Requires: usbutils
Requires: usermode
Requires: utempter
Requires: util-linux
Requires: vconfig
Requires: vim-common
Requires: vim-enhanced
Requires: vim-minimal
Requires: vixie-cron
Requires: wget
Requires: which
Requires: whiptail
Requires: wireless-tools
Requires: words
Requires: xinetd
Requires: xmlsec1
Requires: xmlsec1-openssl
Requires: xorg-x11-libs
Requires: xorg-x11-Mesa-libGL
Requires: yum
Requires: zip
Requires: zlib
# END include requires.txt

%changelog
* Sat Jul 4 2005 Shad L. Lords
- [1.4.4-06sme03]
- Remove e-smith-rp-pppoe as e-smith-base provides this now
- Change perl-MIME-Tools to perl-MIME-tools
- Remove perl-Mail-SpamAssassin

* Sat Jul 2 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.4.4-06sme02]
- Remove centos-yumconf, add centos-release to Requires:

* Fri Jul 1 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.4.4-06sme01]
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
e-smith module to display support and licensing information

%prep
%setup
rm -f root/etc/e-smith/web/common/e-smith-manager.gif
%patch0 -p1
%patch1 -p1

%build
perl createlinks

mkdir -p root/etc/e-smith/licenses/{fr_CA,fr}
cp root/etc/e-smith/licenses/{en_US,fr_CA}/00Unsupported
cp root/etc/e-smith/licenses/{en_US,fr}/00Unsupported

LEXICONS=$(find root/etc/e-smith/locale -type f | grep -v CVS)

for lexicon in $LEXICONS
do
    /sbin/e-smith/validate-lexicon $lexicon
done

for lang in en-us es fr
do
  mkdir -p root/etc/e-smith/locale/${lang}/etc/e-smith/web/functions
  ln -s initial.cgi root/etc/e-smith/locale/${lang}/etc/e-smith/web/functions/index.cgi
done

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%preun
%post
%postun

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
