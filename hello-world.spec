# Short-handed ifdef()
%{!?_sourcedir: %define _sourcedir $(pwd)}

Name:           hello-world
Version:        1.0.0
Release:        1%{?dist}
Summary:        Simple "Hello World" C++ RPM
License:	None
URL:            https://github.com/msteppe91/hello-world

BuildRequires:  gcc

%description
Simple "Hello World" C++ application written to test RPMs on Fedora

%prep
echo "Source dir set to '%{_sourcedir}'"

%build
# TODO: Write Makefile for C++ app instead of manual gcc call
#%make_build
g++ %{_sourcedir}/helloWorld.cpp -o hello

%install
rm -rf $RPM_BUILD_ROOT
# TODO: Add install rule to Makefile when created
#%make_install
install -m 755 %{_builddir}/hello %{buildroot}

%files
/usr/local/bin/hello

%changelog
* Fri Apr  3 2020 Michael Steppe <msteppe91@gmail.com>
- 
