#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mash
Version  : 0.6.19
Release  : 14
URL      : http://pkgs.fedoraproject.org/repo/pkgs/mash/mash-0.6.19.tar.gz/9c72ff746ee287957b2885ed7ccf162e/mash-0.6.19.tar.gz
Source0  : http://pkgs.fedoraproject.org/repo/pkgs/mash/mash-0.6.19.tar.gz/9c72ff746ee287957b2885ed7ccf162e/mash-0.6.19.tar.gz
Summary  : Build system -> repository tool
Group    : Development/Tools
License  : GPL-2.0
Requires: mash-bin
Requires: mash-python3
Requires: mash-data
Requires: mash-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
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
Requires: mash-python3

%description python
python components for the mash package.


%package python3
Summary: python3 components for the mash package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mash package.


%prep
%setup -q -n mash-0.6.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507156729
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
