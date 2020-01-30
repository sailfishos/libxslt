Name:       libxslt
Summary:    Library providing the Gnome XSLT engine
Version:    1.1.33
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://xmlsoft.org/XSLT/
Source0:    ftp://xmlsoft.org/XSLT/libxslt-%{version}.tar.gz
Patch1:     0001-patch-xslt-config-to-add-private-libraries.patch
Patch2:     0002-Fix-security-framework-bypass.patch
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
Obsoletes: %{name}-python <= 1.1.33

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package devel
Summary:  Libraries, includes, etc. to embed the Gnome XSLT engine
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
Man pages and documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

# 0001-patch-xslt-config-to-add-private-libraries.patch
%patch1 -p1
# 0002-Fix-security-framework-bypass.patch
%patch2 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure						\
	--disable-static				\
	--with-python=no                                \
	--docdir=%{_docdir}/%{name}-%{version}

# Call make instruction with smp support
make %{_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

install -m0644 -t $RPM_BUILD_ROOT%{_docdir}/%{name}-1*/ \
    AUTHORS ChangeLog FEATURES README NEWS TODO

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license Copyright
%{_libdir}/lib*.so.*
%{_libdir}/libxslt-plugins
/usr/bin/xsltproc

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_libdir}/*.sh
/usr/share/aclocal/libxslt.m4
/usr/include/*
/usr/bin/xslt-config
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc

%files doc
%defattr(-, root, root)
%doc %{_mandir}/man1/xsltproc.1*
%doc %{_mandir}/man3/libxslt.3*
%doc %{_mandir}/man3/libexslt.3*
%doc %{_docdir}/%{name}-1*/*
