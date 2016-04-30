#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mash
Version  : 0.5.33
Release  : 8
URL      : http://pkgs.fedoraproject.org/repo/pkgs/mash/mash-0.5.33.tar.gz/6c5fc4f8b055c1ddc2fd6ed744cd9273/mash-0.5.33.tar.gz
Source0  : http://pkgs.fedoraproject.org/repo/pkgs/mash/mash-0.5.33.tar.gz/6c5fc4f8b055c1ddc2fd6ed744cd9273/mash-0.5.33.tar.gz
Summary  : Build system -> repository tool
Group    : Development/Tools
License  : GPL-2.0
Requires: mash-bin
Requires: mash-python
Requires: mash-data
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
mash is a tool that queries a koji buildsystem for the latest RPMs for
any particular tag, and creates repositories of those RPMs, including
any multlib RPMs that are necessary.

%package bin
Summary: bin components for the mash package.
Group: Binaries
Requires: mash-data

%description bin
bin components for the mash package.


%package data
Summary: data components for the mash package.
Group: Data

%description data
data components for the mash package.


%package python
Summary: python components for the mash package.
Group: Default

%description python
python components for the mash package.


%prep
%setup -q -n mash-0.5.33

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mash.py

%files data
%defattr(-,root,root,-)
/usr/share/mash/spam-o-matic

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
