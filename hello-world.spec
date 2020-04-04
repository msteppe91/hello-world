Name:           hello-world
Version:        1.0.0
Release:        1%{?dist}
Summary:        Simple "Hello World" C++ RPM
License:        None
URL:            https://github.com/msteppe91/hello-world
AutoReqProv:    no

BuildRequires:  gcc

%description
Simple "Hello World" C++ application written to test RPMs on Fedora

%prep
# Move source to %%_builddir (make sure it's empty first) and compile there
%{__rm} -rf %{_builddir}/*
%{__cp} -a %{_sourcedir}/* %{_builddir}

%build
%make_build

%install
%make_install DESTDIR=%{buildroot}/usr/local/bin/

%files
/usr/local/bin/hello

