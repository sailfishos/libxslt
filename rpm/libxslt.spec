Name:       libxslt
Summary:    Library providing the Gnome XSLT engine
Version:    1.1.29
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://xmlsoft.org/XSLT/
Source0:    ftp://xmlsoft.org/XSLT/libxslt-%{version}.tar.gz
Patch2:     0001-patch-xslt-config-to-add-private-libraries.patch
Patch3:     0002-fix-autoconf-automake.patch
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27
BuildRequires:  python2-devel
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

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

%package python
Summary:  Python bindings for the libxslt library
Group:    Development/Libraries
Requires: libxslt = %{version}-%{release}
Requires: libxml2-python

%description python
The libxslt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxslt library to apply XSLT transformations.

This library allows to parse sytlesheets, uses the libxml2-python
to load and save XML and HTML files. Direct access to XPath and
the XSLT transformation context are possible to extend the XSLT language
with XPath functions written in Python.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
Man pages and documentation for %{name} and %{name}-python.

%prep
%setup -q -n %{name}-%{version}/%{name}

# 0001-patch-xslt-config-to-add-private-libraries.patch
%patch2 -p1
# 0002-fix-autoconf-automake.patch
%patch3 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure						\
	--disable-static				\
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

# Should we make a libxslt-python-devel separate subpackage?

%{_libdir}/lib*.so
%{_libdir}/*.sh
/usr/share/aclocal/libxslt.m4
/usr/include/*
/usr/bin/xslt-config
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc

%files python
%defattr(-, root, root,-)
%{python_sitearch}/libxslt.py*
%{python_sitearch}/libxsltmod*
%doc python/libxsltclass.txt
%doc python/tests/*.py
%doc python/tests/*.xml
%doc python/tests/*.xsl

%files doc
%defattr(-, root, root)
%doc %{_mandir}/man1/xsltproc.1*
%doc %{_mandir}/man3/libxslt.3*
%doc %{_mandir}/man3/libexslt.3*
%doc %{_docdir}/%{name}-1*/*
%doc %{_docdir}/%{name}-python-*/TODO
%doc %{_docdir}/%{name}-python-*/examples/*
