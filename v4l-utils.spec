# libv4l2 is used by ffmpeg, ffmpeg is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 0
%define oldlibname %mklibname v4l 0
%define libname %mklibname v4l
%define develname %mklibname v4l -d
%define wrappersname %mklibname v4l-wrappers
%define devel32name %mklib32name v4l -d
%define wrappers32name %mklib32name v4l-wrappers
%define _disable_rebuild_configure 1
%define _disable_ld_no_undefined 1
%define _disable_lto 1
%bcond_without graphics

Name:		v4l-utils
Version:	1.26.1
Release:	1
Summary:	Linux V4L2 and DVB API utilities
License:	LGPLv2+
Group:		System/Libraries
Url:		http://git.linuxtv.org/v4l-utils.git
Source0:	http://linuxtv.org/downloads/v4l-utils/%{name}-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
#Patch0:		v4l-utils-1.12.3-pthread.patch
#Patch1:		v4l-utils-1.8.0-use-system-jpeg.patch
#Patch2:		v4l-utils-1.20.0-qt-gles.patch

BuildRequires:	meson
BuildRequires:  gettext
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	sysfsutils-devel
BuildRequires:	pkgconfig(libelf)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(json-c) >= 0.15
%if %{with graphics}
BuildRequires:  qmake5
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5OpenGL)
%endif
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libbpf) >= 0.7
BuildRequires:	pkgconfig(systemd)
BuildRequires:	doxygen
Conflicts:	ivtv-utils < 1.4.0-2
Obsoletes:	libv4l < 0.6.4-2
Requires:	%{wrappersname} >= %{version}-%{release}

%define oldname %mklibname v4l 0
Obsoletes:	%{oldname} < %{EVRD}

%if %{with compat32}
BuildRequires:	devel(libjson-c)
BuildRequires:	devel(libjpeg)
BuildRequires:	devel(libelf)
BuildRequires:	devel(libX11)
BuildRequires:	devel(libGL)
BuildRequires:	devel(libGLU)
BuildRequires:	devel(libasound)
BuildRequires:	devel(libudev)
BuildRequires:	libc6
%endif

%description
v4l-utils is the combination of various v4l and dvb utilities which
used to be part of the v4l-dvb mercurial kernel tree. 

%define olddvbv5 %mklibname dvbv5 0
%define dvbv5 %mklibname dvbv5
%define oldv4l1 %mklibname v4l1 0
%define v4l1 %mklibname v4l1
%define oldv4l2 %mklibname v4l2 0
%define v4l2 %mklibname v4l2
%define oldv4l2rds %mklibname v4l2rds 0
%define v4l2rds %mklibname v4l2rds
%define oldv4lconvert %mklibname v4lconvert 0
%define v4lconvert %mklibname v4lconvert

%define dvbv5d %mklibname dvbv5 -d
%define v4l1d %mklibname v4l1 -d
%define v4l2d %mklibname v4l2 -d
%define v4l2rdsd %mklibname v4l2rds -d
%define v4lconvertd %mklibname v4lconvert -d

%define olddvbv532 %mklib32name dvbv5 0
%define dvbv532 %mklib32name dvbv5
%define oldv4l132 %mklib32name v4l1 0
%define v4l132 %mklib32name v4l1
%define oldv4l232 %mklib32name v4l2 0
%define v4l232 %mklib32name v4l2
%define oldv4l2rds32 %mklib32name v4l2rds 0
%define v4l2rds32 %mklib32name v4l2rds
%define oldv4lconvert32 %mklib32name v4lconvert 0
%define v4lconvert32 %mklib32name v4lconvert

%define dvbv5d32 %mklib32name dvbv5 -d
%define v4l1d32 %mklib32name v4l1 -d
%define v4l2d32 %mklib32name v4l2 -d
%define v4l2rdsd32 %mklib32name v4l2rds -d
%define v4lconvertd32 %mklib32name v4lconvert -d

%libpackage dvbv5 %{major}
%{_libdir}/libdvbv5.so

%libpackage v4l1 %{major}
%{_libdir}/libv4l1.so

%libpackage v4l2 %{major}
%{_libdir}/libv4l2.so

%libpackage v4l2rds %{major}
%{_libdir}/libv4l2rds.so

%libpackage v4lconvert %{major}
%{_libdir}/libv4lconvert.so

%define libv4l2tracer %mklibname v4l2tracer
%package -n %{libv4l2tracer}
Summary: Video4Linux tracing library

%description -n %{libv4l2tracer}
Video4Linux tracing library

%files -n %{libv4l2tracer}
%{_libdir}/libv4l2tracer.so

%if %{with compat32}
%lib32package dvbv5 %{major}
%{_prefix}/lib/libdvbv5.so

%lib32package v4l1 %{major}
%{_prefix}/lib/libv4l1.so

%lib32package v4l2 %{major}
%{_prefix}/lib/libv4l2.so

%lib32package v4l2rds %{major}
%{_prefix}/lib/libv4l2rds.so

%lib32package v4lconvert %{major}
%{_prefix}/lib/libv4lconvert.so

%define lib32v4l2tracer %mklib32name v4l2tracer
%package -n %{lib32v4l2tracer}
Summary: 32-Bit Video4Linux tracing library

%description -n %{lib32v4l2tracer}
32-Bit Video4Linux tracing library

%files -n %{lib32v4l2tracer}
%{_prefix}/lib/libv4l2tracer.so
%endif

%package -n v4l-utils-qt5
Summary:	Qt5 tools for v4l applications
Group:		System/Libraries
Conflicts:	libv4l <= 0.7.91-1mdv2010.1
Obsoletes:	v4l-utils-qt4 < 1.16.3-1
Provides:	v4l-utils-qt4 = %{EVRD}

%description -n v4l-utils-qt5
v4l-utils-qt5 is a QT5 gui for the v4l-utils tools.

%package -n %{wrappersname}
Summary:	Wrappers for v4l applications
Group:		System/Libraries
Conflicts:	libv4l <= 0.5.9-1mdv2010.0
Provides:	v4l-wrappers

%description -n %{wrappersname}
This package contains wrapper libraries that adds v4l2 device
compatibility for v4l1 applications and support for various
pixelformats to v4l2 applications.

%package -n %{libname}
Summary:	Thin abstraction layer for video4linux2 devices
Group:		System/Libraries
Requires:	%{name} >= %{version}
Requires:	%{dvbv5} = %{EVRD}
Requires:	%{v4l1} = %{EVRD}
Requires:	%{v4l2} = %{EVRD}
Requires:	%{v4l2rds} = %{EVRD}
Requires:	%{v4lconvert} = %{EVRD}
%rename %{oldlibname}
Obsoletes:	%{olddvbv5} < %{EVRD}
Obsoletes:	%{oldv4l1} < %{EVRD}
Obsoletes:	%{oldv4l2} < %{EVRD}
Obsoletes:	%{oldv4l2rds} < %{EVRD}
Obsoletes:	%{oldv4lconvert} < %{EVRD}

%description -n %{libname}
libv4l is a collection of libraries which adds a thin abstraction
layer on top of video4linux2 devices. The purpose of this (thin)
layer is to make it easy for application writers to support a wide
variety of devices without having to write separate code for
different devices in the same class.

%package -n %{dvbv5d}
Summary:	Development files for libdvbv5
Group:		Development/C
Requires:	%{dvbv5} = %{EVRD}

%description -n %{dvbv5d}
Development files for libdvbv5.

%files -n %{dvbv5d}
%{_includedir}/libdvbv5
%{_libdir}/pkgconfig/libdvbv5.pc

%package -n %{v4l1d}
Summary:	Development files for libv4l1
Group:		Development/C
Requires:	%{v4l1} = %{EVRD}

%description -n %{v4l1d}
Development files for libv4l1.

%files -n %{v4l1d}
%{_includedir}/libv4l1.h
%{_includedir}/libv4l1-videodev.h
%{_libdir}/pkgconfig/libv4l1.pc

%package -n %{v4l2d}
Summary:	Development files for libv4l2
Group:		Development/C
Requires:	%{v4l2} = %{EVRD}

%description -n %{v4l2d}
Development files for libv4l2.

%files -n %{v4l2d}
%{_includedir}/libv4l2.h
%{_includedir}/libv4l-plugin.h
%{_libdir}/pkgconfig/libv4l2.pc

%package -n %{v4l2rdsd}
Summary:	Development files for libv4l2rds
Group:		Development/C
Requires:	%{v4l2rds} = %{EVRD}

%description -n %{v4l2rdsd}
Development files for libv4l2rds.

%files -n %{v4l2rdsd}
%{_includedir}/libv4l2rds.h
%{_libdir}/pkgconfig/libv4l2rds.pc

%package -n %{v4lconvertd}
Summary:	Development files for libv4lconvert
Group:		Development/C
Requires:	%{v4lconvert} = %{EVRD}

%description -n %{v4lconvertd}
Development files for libv4lconvert.

%files -n %{v4lconvertd}
%{_includedir}/libv4lconvert.h
%{_libdir}/pkgconfig/libv4lconvert.pc

%package -n %{develname}
Summary:	Development files from libv4l
Group:		Development/C
Requires:	%{dvbv5d} = %{EVRD}
Requires:	%{v4l1d} = %{EVRD}
Requires:	%{v4l2d} = %{EVRD}
Requires:	%{v4l2rdsd} = %{EVRD}
Requires:	%{v4lconvertd} = %{EVRD}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libv4l-devel = %{version}-%{release}

%description -n %{develname}
This package contains the development files needed to build
programs that use libv4l.

%if %{with compat32}
%package -n %{dvbv5d32}
Summary:	Development files for libdvbv5 (32-bit)
Group:		Development/C
Requires:	%{dvbv532} = %{EVRD}

%description -n %{dvbv5d32}
Development files for libdvbv5.

%files -n %{dvbv5d32}
%{_prefix}/lib/pkgconfig/libdvbv5.pc

%package -n %{v4l1d32}
Summary:	Development files for libv4l1 (32-bit)
Group:		Development/C
Requires:	%{v4l132} = %{EVRD}

%description -n %{v4l1d32}
Development files for libv4l1.

%files -n %{v4l1d32}
%{_prefix}/lib/pkgconfig/libv4l1.pc

%package -n %{v4l2d32}
Summary:	Development files for libv4l2 (32-bit)
Group:		Development/C
Requires:	%{v4l232} = %{EVRD}

%description -n %{v4l2d32}
Development files for libv4l2.

%files -n %{v4l2d32}
%{_prefix}/lib/pkgconfig/libv4l2.pc

%package -n %{v4l2rdsd32}
Summary:	Development files for libv4l2rds (32-bit)
Group:		Development/C
Requires:	%{v4l2rds32} = %{EVRD}

%description -n %{v4l2rdsd32}
Development files for libv4l2rds.

%files -n %{v4l2rdsd32}
%{_prefix}/lib/pkgconfig/libv4l2rds.pc

%package -n %{v4lconvertd32}
Summary:	Development files for libv4lconvert (32-bit)
Group:		Development/C
Requires:	%{v4lconvert32} = %{EVRD}

%description -n %{v4lconvertd32}
Development files for libv4lconvert.

%files -n %{v4lconvertd32}
%{_prefix}/lib/pkgconfig/libv4lconvert.pc

%package -n %{devel32name}
Summary:	Development files from libv4l (32-bit)
Group:		Development/C
Requires:	%{dvbv5d32} = %{EVRD}
Requires:	%{v4l1d32} = %{EVRD}
Requires:	%{v4l2d32} = %{EVRD}
Requires:	%{v4l2rdsd32} = %{EVRD}
Requires:	%{v4lconvertd32} = %{EVRD}
Obsoletes:	%{olddvbv532} < %{EVRD}
Obsoletes:	%{oldv4l132} < %{EVRD}
Obsoletes:	%{oldv4l232} < %{EVRD}
Obsoletes:	%{oldv4l2rds32} < %{EVRD}
Obsoletes:	%{oldv4lconvert32} < %{EVRD}

%description -n %{devel32name}
This package contains the development files needed to build
programs that use libv4l.

%package -n %{wrappers32name}
Summary:	Wrappers for v4l applications
Group:		System/Libraries

%description -n %{wrappers32name}
This package contains wrapper libraries that adds v4l2 device
compatibility for v4l1 applications and support for various
pixelformats to v4l2 applications.

%files -n %{wrappers32name}
%dir %{_prefix}/lib/libv4l
%dir %{_prefix}/lib/libv4l/plugins
%{_prefix}/lib/libv4l/*-decomp
%{_prefix}/lib/libv4l/plugins/libv4l-mplane.so
%{_prefix}/lib/v4l1compat.so
%{_prefix}/lib/v4l2convert.so
%{_prefix}/lib/libv4l/v4l1compat.so
%{_prefix}/lib/libv4l/v4l2convert.so
%endif

%prep
%autosetup -p1

%if %{with compat32}
%meson32 --debug \
                  -Dqv4l2=disabled \
                  -Dqvidcap=disabled \
                  -Dbpf=disabled \
                  -Dgconv=disabled
%endif

%meson  \
        -Dgconv=disabled

%build
%if %{with compat32}
%ninja_build -C build32
%endif
%meson_build

%install
%if %{with compat32}
%ninja_install -C build32
%endif
%meson_install

# already provided by ivtv-utils package, more uptodate/complete there
rm -f %{buildroot}%{_bindir}/ivtv-ctl

%find_lang %{name}
%find_lang libdvbv5
cat *.lang >%{name}-all.lang

%files -f %{name}-all.lang
%config(noreplace) %{_sysconfdir}/rc_maps.cfg
%config(noreplace) %{_udevrulesdir}/70-infrared.rules
%dir %(dirname %{_udevrulesdir})/rc_keymaps
%{_udevrulesdir}/../rc_keymaps/*
#{_prefix}/lib/systemd/system/systemd-udevd.service.d/50-rc_keymap.conf
%{_bindir}/cec-compliance
%{_bindir}/cec-ctl
%{_bindir}/cec-follower
%{_bindir}/dvbv5-daemon
%{_bindir}/ir-ctl
%{_bindir}/cx18-ctl
%{_bindir}/decode_tm6000
%{_bindir}/ir-keytable
%{_bindir}/rds-ctl
%{_bindir}/v4l2-compliance
%{_bindir}/v4l2-ctl
%{_bindir}/v4l2-tracer
%{_bindir}/dvb-fe-tool
%{_bindir}/dvb-format-convert
%{_bindir}/dvbv5-scan
%{_bindir}/dvbv5-zap
%{_bindir}/v4l2-sysfs-path
%{_bindir}/media-ctl
#{_sbindir}/v4l2-dbg
%doc %{_mandir}/man1/ir-keytable.1*
%doc %{_mandir}/man1/dvb-fe-tool.1*
%doc %{_mandir}/man1/dvb-format-convert.1*
%doc %{_mandir}/man1/dvbv5-scan.1*
%doc %{_mandir}/man1/dvbv5-zap.1*
%doc %{_mandir}/man1/v4l2-compliance.1*
%doc %{_mandir}/man1/v4l2-ctl.1*
%doc %{_mandir}/man1/v4l2-tracer.1*
%doc %{_mandir}/man1/cec-compliance.1*
%doc %{_mandir}/man1/cec-ctl.1*
%doc %{_mandir}/man1/cec-follower.1*
%doc %{_mandir}/man1/ir-ctl.1*
%doc %{_mandir}/man5/rc_keymap.5*

%files -n v4l-utils-qt5
%if %{with graphics}
%{_bindir}/qv4l2
%{_datadir}/applications/qv4l2.desktop
%{_iconsdir}/hicolor/*/apps/qv4l2.*
%doc %{_mandir}/man1/qv4l2.1*
%{_bindir}/qvidcap
%{_datadir}/applications/qvidcap.desktop
%{_iconsdir}/hicolor/*/apps/qvidcap.*g
%doc %{_mandir}/man1/qvidcap.1*
%endif

%files -n %{wrappersname}
%dir %{_libdir}/libv4l
%dir %{_libdir}/libv4l/plugins
%{_libdir}/v4l1compat.so
%{_libdir}/v4l2convert.so
%{_libdir}/libv4l/v4l1compat.so
%{_libdir}/libv4l/v4l2convert.so
%{_libdir}/libv4l/*-decomp
%{_libdir}/libv4l/plugins/libv4l-mplane.so

%files -n %{libname}

%files -n %{develname}
