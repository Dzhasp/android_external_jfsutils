Name      : jfsutils
Version   : 1.1.14
Release   : 1
Group     : System/Kernel

Summary   : IBM JFS utility programs

Copyright : GPL
Packager  : JFS/Linux team <shaggy@linux.vnet.ibm.com>
URL       : http://jfs.sourceforge.net/

Buildroot : %{_tmppath}/%{name}-%{version}
Source    : %{name}-%{version}.tar.gz


%Description
Utilities for managing IBM's Journaled File System (JFS) under Linux.  The
following utilities are available: jfs_fsck - initiate replay of the JFS
transaction log, and check and repair a JFS formatted device. jfs_fscklog -
extract a log from the JFS fsck workspace into a file and/or display it.
jfs_logdump - dump a JFS formatted device's journal log. jfs_mkfs - create
a JFS formatted partition. jfs_tune - adjust tunable parameters of the JFS
file system. jfs_debugfs - shell-type JFS file system editor.


%Prep
%setup -q

%Build
CFLAGS="${RPM_OPT_FLAGS}" ./configure --mandir=/usr/share/man/en/
make

%Install
make install DESTDIR=${RPM_BUILD_ROOT}

%Clean
rm -rf ${RPM_BUILD_ROOT}

%Files
%defattr(-,root,root)
/sbin/*
%{_mandir}/en/man8/*
%doc AUTHORS COPYING INSTALL NEWS README ChangeLog
