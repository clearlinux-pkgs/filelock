#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : filelock
Version  : 3.3.1
Release  : 26
URL      : https://files.pythonhosted.org/packages/8f/eb/6faad9294c8a8d59b7599a8a7c669c0e4c317fa5012bc36f1c8b379972a5/filelock-3.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8f/eb/6faad9294c8a8d59b7599a8a7c669c0e4c317fa5012bc36f1c8b379972a5/filelock-3.3.1.tar.gz
Summary  : A platform independent file lock.
Group    : Development/Tools
License  : Unlicense
Requires: filelock-license = %{version}-%{release}
Requires: filelock-python = %{version}-%{release}
Requires: filelock-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
# py-filelock
[![PyPI](https://img.shields.io/pypi/v/filelock?style=flat-square)](https://pypi.org/project/filelock/)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/filelock.svg)](https://pypi.org/project/filelock/)
[![Documentation
status](https://readthedocs.org/projects/py-filelock/badge/?version=latest&style=flat-square)](https://py-filelock.readthedocs.io/en/latest/?badge=latest)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://pepy.tech/badge/filelock/month)](https://pepy.tech/project/filelock/month)
[![check](https://github.com/tox-dev/py-filelock/actions/workflows/check.yml/badge.svg)](https://github.com/tox-dev/py-filelock/actions/workflows/check.yml)

%package license
Summary: license components for the filelock package.
Group: Default

%description license
license components for the filelock package.


%package python
Summary: python components for the filelock package.
Group: Default
Requires: filelock-python3 = %{version}-%{release}

%description python
python components for the filelock package.


%package python3
Summary: python3 components for the filelock package.
Group: Default
Requires: python3-core
Provides: pypi(filelock)

%description python3
python3 components for the filelock package.


%prep
%setup -q -n filelock-3.3.1
cd %{_builddir}/filelock-3.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635172051
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/filelock
cp %{_builddir}/filelock-3.3.1/LICENSE %{buildroot}/usr/share/package-licenses/filelock/24944bf7920108f5a4790e6071c32e9102760c37
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/filelock/24944bf7920108f5a4790e6071c32e9102760c37

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
