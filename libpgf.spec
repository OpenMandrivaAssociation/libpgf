%define major 6
%define libname %mklibname pgf %{major}
%define libnamedev %mklibname pgf -d


Name:            libpgf
Summary:         PGF (Progressive Graphics File) library
Group:           System/Libraries
Version:         6.14.12
Release:         7
License:         LGPLv2+
URL:             https://www.libpgf.org
Source0:         http://downloads.sourceforge.net/project/%{name}/%{version}/%{name}-src-%{version}.tar.gz
BuildRequires:   doxygen
BuildRequires:   libtool
BuildRequires:	dos2unix

%description
libPGF contains an implementation of the Progressive Graphics File (PGF)
which is a new image file format, that is based on a discrete, fast
wavelet transform with progressive coding features. PGF can be used
for lossless and lossy compression.

#-------------------------------------------------------------------
%package -n %{libname}
Summary:         PGF library
Group:           System/Libraries

%description -n %{libname}
libPGF contains an implementation of the Progressive Graphics File (PGF)
which is a new image file format, that is based on a discrete, fast
wavelet transform with progressive coding features. PGF can be used
for lossless and lossy compression.

%files -n %{libname}
%{_libdir}/libpgf.so.%{major}*

#--------------------------------------------------------------------
%package doc
Summary:         libpgf Documentation
BuildArch:       noarch

%description doc
libPGF contains an implementation of the Progressive Graphics File (PGF)
which is a new image file format, that is based on a discrete, fast
wavelet transform with progressive coding features. PGF can be used
for lossless and lossy compression.

%files doc
%doc AUTHORS COPYING NEWS README
%doc %{_docdir}/%{name}-%{version}
%{_mandir}/man3/*

#--------------------------------------------------------------------
%package -n %{libnamedev}
Summary:        libpgf Development Files
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
libPGF contains an implementation of the Progressive Graphics File (PGF)
which is a new image file format, that is based on a discrete, fast
wavelet transform with progressive coding features. PGF can be used
for lossless and lossy compression.

%files -n %{libnamedev}
%{_includedir}/%{name}
%{_libdir}/libpgf.so
%{_libdir}/pkgconfig/libpgf.pc

#------------------------------------------------------------------------------
%prep
%setup -qn %{name}

%build
dos2unix configure.ac
sh autogen.sh
%configure 
%make

%install
%makeinstall_std

#find %{buildroot} -name '*.la' -exec rm -f {} ';'

