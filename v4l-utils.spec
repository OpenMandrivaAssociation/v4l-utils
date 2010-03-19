%define major		0
%define libname		%mklibname v4l %{major}
%define develname	%mklibname v4l -d
%define wrappersname	%mklibname v4l-wrappers

Name:		v4l-utils
Version:	0.7.91
Release:	%mkrel 1
Summary:	Linux V4L2 and DVB API utilities
License:	LGPLv2+
Group:		System/Libraries
URL:		http://git.linuxtv.org/v4l-utils.git
Source:		http://people.fedoraproject.org/~jwrdegoede/v4l-utils-%{version}.tar.bz2
BuildRequires:	qt4-devel
Obsoletes:	libv4l <= 0.6.4-1mdv2010.1
Requires:	%{wrappersname} >= %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
v4l-utils is the combination of various v4l and dvb utilities which
used to be part of the v4l-dvb mercurial kernel tree. 

%files
%defattr(0755,root,root,0755)
%{_bindir}/cx18-ctl
%{_bindir}/decode_tm6000
%{_bindir}/ivtv-ctl
%{_bindir}/qv4l2
%{_bindir}/v4l2-compliance
%{_bindir}/v4l2-ctl
%{_bindir}/v4l2-sysfs-path
%{_sbindir}/v4l2-dbg

%package -n	%{wrappersname}
Summary:	Wrappers for v4l applications
Group:		System/Libraries
Conflicts:	libv4l <= 0.5.9-1mdv2010.0

%description -n %{wrappersname}
This package contains wrapper libraries that adds v4l2 device compatibility for
v4l1 applications and support for various pixelformats to v4l2 applications.

%files -n	%{wrappersname}
%defattr(0644,root,root,0755)
%dir %{_libdir}/libv4l
%{_libdir}/libv4l/v4l1compat.so
%{_libdir}/libv4l/v4l2convert.so
%{_libdir}/libv4l/*-decomp

%package -n	%{libname}
Summary:	Thin abstraction layer for video4linux2 devices
Group:		System/Libraries
Requires:	%name >= %version

%description -n %{libname}
libv4l is a collection of libraries which adds a thin abstraction layer on top
of video4linux2 devices. The purpose of this (thin) layer is to make it easy for
application writers to support a wide variety of devices without having to write
separate code for different devices in the same class.

%files -n	%{libname}
%defattr(0644,root,root,0755)
%{_libdir}/libv4l1.so.%{major}*
%{_libdir}/libv4l2.so.%{major}*
%{_libdir}/libv4lconvert.so.%{major}*

%package -n	%{develname}
Summary:	Development files from libv4l
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the development files needed to build programs that use
libv4l.

%files -n	%{develname}
%defattr(0644,root,root,0755)
%{_includedir}/libv4l1.h
%{_includedir}/libv4l2.h
%{_includedir}/libv4lconvert.h
%{_libdir}/libv4l1.so
%{_libdir}/libv4l2.so
%{_libdir}/libv4lconvert.so
%{_libdir}/pkgconfig/libv4l1.pc
%{_libdir}/pkgconfig/libv4l2.pc
%{_libdir}/pkgconfig/libv4lconvert.pc

%prep
%setup -q

%build
%make CFLAGS="%{optflags}" PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

