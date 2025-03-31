Name:       libxslt
Summary:    Library providing the Gnome XSLT engine
Version:    1.1.43
Release:    1
License:    MIT
URL:        https://github.com/sailfishos/libxslt
Source0:    %{name}-%{version}.tar.gz
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27
BuildRequires:  cmake
Obsoletes: %{name}-python <= 1.1.33

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine.

%package devel
Summary:  Libraries, includes, etc. to embed the Gnome XSLT engine
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Man pages and documentation for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
mkdir -p _build
pushd _build
%cmake .. \
    -DLIBXSLT_WITH_PYTHON=OFF \
    -DLIBXSLT_WITH_TESTS=OFF

%make_build
popd

%install
pushd _build
%make_install
popd

mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}-plugins

# Remove devhelp documentation
rm -Rf $RPM_BUILD_ROOT%{_docdir}/%{name}/devhelp
rm -Rf $RPM_BUILD_ROOT%{_docdir}/%{name}/EXSLT/devhelp

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license Copyright
%{_libdir}/lib*.so.*
%{_libdir}/%{name}-plugins
%{_bindir}/xsltproc

%files devel
%{_libdir}/lib*.so
%{_libdir}/*.sh
%{_includedir}/*
%{_bindir}/xslt-config
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/libexslt.pc
%{_libdir}/cmake/libxslt*/

%files doc
%doc %{_mandir}/man1/xsltproc.1*
%doc %{_mandir}/man3/%{name}.3*
%doc %{_mandir}/man3/libexslt.3*
%doc %{_docdir}/%{name}/*
