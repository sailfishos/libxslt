# 
# Do not Edit! Generated by:
# spectacle version 0.13
# 
# >> macros
# << macros

Name:       libxslt
Summary:    Library providing the Gnome XSLT engine
Version:    1.1.26
Release:    2
Group:      System/Libraries
License:    MIT
URL:        http://xmlsoft.org/XSLT/
Source0:    ftp://xmlsoft.org/XSLT/libxslt-%{version}.tar.gz
Source100:  libxslt.yaml
Patch0:     multilib.patch
Patch1:     0003-code-fix-and-docs-modification.patch
Patch2:     0004-fix-typo.patch
Patch3:     0005-cve-2012-2825.patch
Patch4:     0006-cve-2012-2870.patch
Patch5:     0007-Fix-default-template-processing-on-namespace-nodes.patch
Patch6:     0008-Fix-a-dictionary-string-usage.patch
Patch7:     0009-Fix-crash-with-empty-xsl-key-match-attribute.patch
Patch8:     0010-Crash-when-passing-an-uninitialized-variable-to-docu.patch
Patch9:     libxslt-aarch64.patch
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27
BuildRequires: python2-devel

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine



%package devel
Summary:    Libraries, includes, etc. to embed the Gnome XSLT engine
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed.

%package python
Summary: Python bindings for the libxslt library
Group: Development/Libraries
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



%prep
%setup -q -n %{name}-%{version}

# multilib.patch
%patch0 -p1
# 0003-code-fix-and-docs-modification.patch
%patch1 -p1
# 0004-fix-typo.patch
%patch2 -p1
# 0005-cve-2012-2825.patch
%patch3 -p1
# 0006-cve-2012-2870.patch
%patch4 -p1 
# 0007-Fix-default-template-processing-on-namespace-nodes.patch
%patch5 -p1
# 0008-Fix-a-dictionary-string-usage.patch
%patch6 -p1
# 0009-Fix-crash-with-empty-xsl-key-match-attribute.patch
%patch7 -p1
# 0010-Crash-when-passing-an-uninitialized-variable-to-docu.patch
%patch8 -p1
%patch9 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
# Call make instruction with smp support
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%defattr(-,root,root,-)
# >> files
%doc Copyright AUTHORS README
%doc %{_mandir}/man1/xsltproc.1*
%{_libdir}/lib*.so.*
%{_libdir}/libxslt-plugins
/usr/bin/xsltproc
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%doc FEATURES Copyright ChangeLog AUTHORS README NEWS TODO
%doc doc/EXSLT
%doc %{_mandir}/man3/libxslt.3*
%doc %{_mandir}/man3/libexslt.3*
%{_libdir}/lib*.so
%{_libdir}/*.sh
/usr/share/aclocal/libxslt.m4
/usr/include/*
/usr/bin/xslt-config
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc
# << files devel

%files python
%defattr(-, root, root,-)
%{python_sitearch}/libxslt.py*
%{python_sitearch}/libxsltmod*
%doc python/libxsltclass.txt
%doc python/tests/*.py
%doc python/tests/*.xml
%doc python/tests/*.xsl

