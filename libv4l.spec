%define major		0
%define libname		%mklibname v4l %{major}
%define develname	%mklibname v4l -d
%define wrappersname	%mklibname v4l-wrappers

Name:		libv4l
Version:	0.6.4
Release:	%mkrel 1
Summary:	Thin abstraction layer for video4linux2 devices
License:	LGPLv2+
Group:		System/Libraries
URL:		http://hansdegoede.livejournal.com/3636.html
Source:		http://people.fedoraproject.org/~jwrdegoede/libv4l-%{version}.tar.gz
BuildRequires:	glibc-devel
Requires:	%{wrappersname} >= %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
libv4l is a collection of libraries which adds a thin abstraction layer on top
of video4linux2 devices. The purpose of this (thin) layer is to make it easy for
application writers to support a wide variety of devices without having to write
separate code for different devices in the same class.

%files
#metapackage, no files

%package -n	%{wrappersname}
Summary:	Wrappers for v4l applications
Group:		System/Libraries
Conflicts:	libv4l <= 0.5.9-1mdv2010.0

%description -n %{wrappersname}
This package contains wrapper libraries that adds v4l2 device compatibility for
v4l1 applications and support for various pixelformats to v4l2 applications.

%files -n	%{wrappersname}
%defattr(0644,root,root,0755)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/v4l1compat.so
%{_libdir}/%{name}/v4l2convert.so
%{_libdir}/%{name}/*-decomp

%package -n	%{libname}
Summary:	Main libraries for libv4l
Group:		System/Libraries
Requires:	%name >= %version

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with libv4l.

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
%{_includedir}/%{name}1.h
%{_includedir}/%{name}2.h
%{_includedir}/%{name}convert.h
%{_libdir}/%{name}1.so
%{_libdir}/%{name}2.so
%{_libdir}/%{name}convert.so
%{_libdir}/pkgconfig/%{name}1.pc
%{_libdir}/pkgconfig/%{name}2.pc
%{_libdir}/pkgconfig/%{name}convert.pc

%prep
%setup -q

%build
%make CFLAGS="%{optflags}" PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

