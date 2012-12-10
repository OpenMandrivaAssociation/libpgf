%define major 4
%define libname %mklibname pgf %{major}
%define libnamedev %mklibname pgf -d


Name:            libpgf
Summary:         PGF (Progressive Graphics File) library
Group:           System/Libraries
Version:         6.11.42
Release:         1
License:         LGPLv2+
URL:             http://www.libpgf.org
Source0:         http://downloads.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}-src.zip
BuildRequires:   doxygen
BuildRequires:   libtool

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
sh -x autogen.sh
%{configure2_5x} --disable-static
%{make}

%install
rm -rf %{buildroot}
%{makeinstall_std}

find %{buildroot} -name '*.la' -exec rm -f {} ';'



%changelog
* Tue Nov 15 2011 Zé <ze@mandriva.org> 6.11.42-1
+ Revision: 730663
- imported package libpgf


* Thu Nov 15 2011 Zé <ze@mandriva.org> 6.11.42-1
- first package
