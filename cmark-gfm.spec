%if 0%{?rhel} && 0%{?rhel} < 7
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           cmark-gfm
Version:        0.28.3.gfm.19
Release:        4%{?dist}
Summary:        CommonMark parsing and rendering with GitHub Flavored Markdown extensions

License:        BSD and MIT
URL:            https://github.com/github/cmark-gfm
Source0:        https://github.com/github/cmark-gfm/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
`cmark-gfm` is the GitHub variant on the C reference implementation of
CommonMark, a rationalized version of Markdown syntax with a spec.

It provides a shared library (`libcmark-gfm`) with functions for parsing
GitHub-flavored Markdown documents to an abstract syntax tree (AST), 
manipulating the AST, and rendering the document to HTML, groff man, 
LaTeX, CommonMark, or an XML representation of the AST.  It also provides 
a command-line program (`cmark-gfm`) for parsing and rendering CommonMark
documents.


%package devel
Summary:        Development files for cmark-gfm
Requires:       cmark-gfm-lib = %{version}-%{release}

%description devel
This package provides the development files for cmark-gfm.



%package lib
Summary:        CommonMark parsing and rendering library

%description lib
This package provides the cmark-gfm library.



%prep
%setup -q


%build
mkdir build
cd build
%cmake %{?_without_tests:-DCMARK_TESTS=OFF} ..
make %{?_smp_mflags}


%install
cd build
make install DESTDIR=%{buildroot}

rm %{buildroot}%{_libdir}/libcmark-gfm.a
rm %{buildroot}%{_libdir}/libcmark-gfm-extensions.a
rm %{buildroot}%{_libdir}/libcmark-gfm-extensions.so


%check
%if %{with tests}
cd build
make test
%endif


%post lib -p /sbin/ldconfig


%postun lib -p /sbin/ldconfig


%files
%license COPYING
%{_bindir}/cmark-gfm
%{_mandir}/man1/cmark-gfm.1.gz


%files lib
%license COPYING
%{_libdir}/libcmark-gfm.so.%{version}
%{_libdir}/libcmark-gfm-extensions.so.%{version}


%files devel
%doc README.md
%{_includedir}/cmark-gfm.h
%{_includedir}/cmark-gfm-core-extensions.h
%{_includedir}/cmark-gfm-extension_api.h
%{_includedir}/cmark-gfm_export.h
%{_includedir}/cmark-gfm-extensions_export.h
%{_includedir}/cmark-gfm_version.h
%{_libdir}/libcmark-gfm.so
%{_libdir}/pkgconfig/libcmark-gfm.pc
%{_mandir}/man3/cmark-gfm.3.gz
%{_libdir}/cmake/cmark-gfm*.cmake
%{_libdir}/cmake-gfm-extensions/cmark-gfm-extensions-release.cmake
%{_libdir}/cmake-gfm-extensions/cmark-gfm-extensions.cmake



%changelog
* Thu Dec 20 2018 Kevin White <k.dub.01@gmail.com> - 0.28.3.gfm.19-1
- initial packaging
- source spec from Fedora cmark srpm
