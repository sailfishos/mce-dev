Name:       mce-headers
Summary:    Development files for mce
Version:    1.32.0
Release:    1
Group:      Development/Libraries
License:    LGPLv2
URL:        https://git.sailfishos.org/mer-core/mce-dev
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires:  doxygen

%description
This package contains headers defining the D-Bus method calls
provided by the Mode Control Entity, and the signals emitted by it.

%package -n mce-doc
Summary:    Documentation files for mce D-Bus API
Group:      Documentation
BuildArch:  noarch

%description -n mce-doc
This package contains documentation describing the D-Bus method calls
provided by the Mode Control Entity, and the signals emitted by it.

%prep
%setup -q -n %{name}-%{version}

%build
./verify_version
make %{?_smp_mflags}
make doc

%install
rm -rf %{buildroot}
make install PCDIR=%{_libdir}/pkgconfig DESTDIR=%{?buildroot}
install -d %{buildroot}/%{_docdir}/mce-doc/html/
install -m 644 doc/html/* %{buildroot}/%{_docdir}/mce-doc/html/

%files
%defattr(-,root,root,-)
%doc COPYING debian/copyright
%{_includedir}/mce/*.h
%{_libdir}/pkgconfig/mce.pc

%files -n mce-doc
%defattr(-,root,root,-)
%doc COPYING debian/changelog debian/copyright
%{_docdir}/mce-doc/html/*
