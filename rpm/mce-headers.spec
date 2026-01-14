Name:       mce-headers
Summary:    Development files for mce
Version:    1.32.1
Release:    1
License:    LGPLv2
URL:        https://github.com/sailfishos/mce-dev
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires:  doxygen

%description
This package contains headers defining the D-Bus method calls
provided by the Mode Control Entity, and the signals emitted by it.

%package -n mce-doc
Summary:    Documentation files for mce D-Bus API
BuildArch:  noarch

%description -n mce-doc
This package contains documentation describing the D-Bus method calls
provided by the Mode Control Entity, and the signals emitted by it.

%prep
%setup -q -n %{name}-%{version}

%build
./verify_version
%make_build
make doc

%install
make install PCDIR=%{_libdir}/pkgconfig DESTDIR=%{?buildroot}
install -d %{buildroot}/%{_docdir}/mce-doc/html/
install -m 644 doc/html/* %{buildroot}/%{_docdir}/mce-doc/html/

%files
%doc COPYING debian/copyright
%{_includedir}/mce/*.h
%{_libdir}/pkgconfig/mce.pc

%files -n mce-doc
%doc COPYING debian/changelog debian/copyright
%{_docdir}/mce-doc/html/*
