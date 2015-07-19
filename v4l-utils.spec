%define major 0
%define libname %mklibname v4l %{major}
%define develname %mklibname v4l -d
%define wrappersname %mklibname v4l-wrappers

Name:		v4l-utils
Version:	1.6.3
Release:	2
Summary:	Linux V4L2 and DVB API utilities
License:	LGPLv2+
Group:		System/Libraries
Url:		http://git.linuxtv.org/v4l-utils.git
Source0:	http://linuxtv.org/downloads/v4l-utils/%{name}-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc
#Patch0:		fix-missing-includes.patch
BuildRequires:	sysfsutils-devel
BuildRequires:	qt4-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(glu)
Conflicts:	ivtv-utils < 1.4.0-2
Obsoletes:	libv4l < 0.6.4-2
Requires:	%{wrappersname} >= %{version}-%{release}

%description
v4l-utils is the combination of various v4l and dvb utilities which
used to be part of the v4l-dvb mercurial kernel tree. 

%package -n	v4l-utils-qt4
Summary:	Qt4 tools for v4l applications
Group:		System/Libraries
Conflicts:	libv4l <= 0.7.91-1mdv2010.1

%description -n	v4l-utils-qt4
v4l-utils-qt4 is a QT4 gui for the v4l-utils tools.

%package -n	%{wrappersname}
Summary:	Wrappers for v4l applications
Group:		System/Libraries
Conflicts:	libv4l <= 0.5.9-1mdv2010.0
Provides:	v4l-wrappers

%description -n %{wrappersname}
This package contains wrapper libraries that adds v4l2 device
compatibility for v4l1 applications and support for various
pixelformats to v4l2 applications.

%package -n	%{libname}
Summary:	Thin abstraction layer for video4linux2 devices
Group:		System/Libraries
Requires:	%{name} >= %{version}

%description -n %{libname}
libv4l is a collection of libraries which adds a thin abstraction
layer on top of video4linux2 devices. The purpose of this (thin)
layer is to make it easy for application writers to support a wide
variety of devices without having to write separate code for
different devices in the same class.

%package -n	%{develname}
Summary:	Development files from libv4l
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libv4l-devel = %{version}-%{release}

%description -n %{develname}
This package contains the development files needed to build
programs that use libv4l.

%prep
%setup -q

%build
%configure \
		--enable-libdvbv5 \
		--disable-static
%make

%install
%makeinstall_std PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

# already provided by ivtv-utils package, more uptodate/complete there
rm -f %{buildroot}%{_bindir}/ivtv-ctl

%files
%config(noreplace) %{_sysconfdir}/rc_maps.cfg
%config(noreplace) /lib/udev/rules.d/70-infrared.rules
%dir /lib/udev/rc_keymaps
/lib/udev/rc_keymaps/*
%{_bindir}/cx18-ctl
%{_bindir}/decode_tm6000
%{_bindir}/ir-keytable
%{_bindir}/rds-ctl
%{_bindir}/v4l2-compliance
%{_bindir}/v4l2-ctl
%{_bindir}/dvb-fe-tool
%{_bindir}/dvb-format-convert
%{_bindir}/dvbv5-scan
%{_bindir}/dvbv5-zap
%{_bindir}/v4l2-sysfs-path
%{_sbindir}/v4l2-dbg
%{_mandir}/man1/ir-keytable.1.*
%{_bindir}/media-ctl
%{_mandir}/man1/dvb-fe-tool.1*
%{_mandir}/man1/dvb-format-convert.1*
%{_mandir}/man1/dvbv5-scan.1*
%{_mandir}/man1/dvbv5-zap.1*

%files -n v4l-utils-qt4
%{_bindir}/qv4l2
%{_datadir}/applications/qv4l2.desktop
%{_iconsdir}/hicolor/*/apps/qv4l2.*
%{_mandir}/man1/qv4l2.1*

%files -n %{wrappersname}
%dir %{_libdir}/libv4l
%dir %{_libdir}/libv4l/plugins
%{_libdir}/libv4l/v4l1compat.so
%{_libdir}/libv4l/v4l2convert.so
%{_libdir}/libv4l/*-decomp
%{_libdir}/libv4l/plugins/libv4l-mplane.so

%files -n %{libname}
%{_libdir}/libv4l1.so.%{major}*
%{_libdir}/libv4l2*.so.%{major}*
%{_libdir}/libdvbv5.so.%{major}*
%{_libdir}/libv4lconvert.so.%{major}*

%files -n %{develname}
%{_includedir}/*.h
%{_includedir}/libdvbv5
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
