# 
# Do not Edit! Generated by:
# spectacle version 0.13
# 
# >> macros
# << macros

Name:       libxslt
Summary:    Library providing the Gnome XSLT engine
Version:    1.1.26
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://xmlsoft.org/XSLT/
Source0:    ftp://xmlsoft.org/XSLT/libxslt-%{version}.tar.gz
Source100:  libxslt.yaml
Patch0:     multilib.patch
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27

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



%prep
%setup -q -n %{name}-%{version}

# multilib.patch
%patch0 -p1
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

