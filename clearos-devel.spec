Name: clearos-devel
Version: 7.1.3
Release: 1%{dist}
Summary: ClearOS developer tools
License: GPLv3
Group: ClearOS/Tools
Source: %{name}-%{version}.tar.gz
Vendor: ClearFoundation
Packager: ClearFoundation
# FIXME: make deps from EPEL optional -- we have broken repos right now.
# "Development tools" in comps.xml
Requires: autoconf
Requires: automake
Requires: binutils
Requires: bison
Requires: flex
Requires: gcc
Requires: gcc-c++
Requires: gettext
Requires: libtool
Requires: make
Requires: patch
Requires: pkgconfig
Requires: redhat-rpm-config
Requires: rpm-build
Requires: byacc
Requires: cscope
Requires: ctags
Requires: cvs
Requires: diffstat
Requires: doxygen
Requires: elfutils
Requires: gcc-gfortran
Requires: git
Requires: indent
Requires: intltool
Requires: patchutils
Requires: rcs
Requires: subversion
Requires: swig
Requires: systemtap
Requires: chrpath
Requires: cmake
Requires: expect
Requires: gcc-gnat
Requires: gcc-objc
Requires: gcc-objc++
Requires: nasm
Requires: rpmdevtools
Requires: rpmlint
Requires: rpm-sign
# Other handy tools
Requires: rsync
Requires: syslinux
# App and install test development
Requires: clearos-base
Requires: clearos-coding-standard
Requires: php-phpunit-PHPUnit
Requires: php-pear-PHP-CodeSniffer
# Build system
Requires: mock
Requires: plague-client
BuildRoot: %_tmppath/%name-%version-buildroot

%description
ClearOS developer tools

%prep
%setup
%build

%install
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/mock
mkdir -p -m 755 $RPM_BUILD_ROOT%{_bindir}

install -m 644 clearos-7-x86_64-base.cfg $RPM_BUILD_ROOT%{_sysconfdir}/mock/

%post
if [ ! -e /usr/bin/clearos ]; then
    echo "#!/bin/sh" > /usr/bin/clearos
    echo "echo \"The clearos script has been moved to app-devel! - yum install app-devel\"" >> /usr/bin/clearos
    chmod 755 /usr/bin/clearos
fi

if [ -e /etc/mock/default.cfg ]; then
    rm -f /etc/mock/default.cfg
fi

ln -s /etc/mock/clearos-7-x86_64-base.cfg /etc/mock/default.cfg

%files
%defattr(-,root,root)
%{_sysconfdir}/mock/clearos-7-x86_64-base.cfg
