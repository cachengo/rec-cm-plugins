# Copyright 2019 Nokia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

Name:		validators
Version:	%{_version}
Release:	1%{?dist}
Summary:	Configuration validators
License:        %{_platform_licence}
Source0:        %{name}-%{version}.tar.gz
Vendor:         %{_platform_vendor}
BuildArch:      noarch
BuildRequires:  python

Requires: python-django, python-ipaddr

%define PKG_BASE_DIR /opt/cmframework/validators

%description
This RPM contains source code for configuration validators

%prep
%autosetup

%install
mkdir -p %{buildroot}/%{PKG_BASE_DIR}/
find validators/src -name '*.py' -exec cp {} %{buildroot}/%{PKG_BASE_DIR}/ \;

%files
%defattr(0755,root,root,0755)
%{PKG_BASE_DIR}/*.py*

%pre

%post

%preun

%postun

%clean
rm -rf %{buildroot}
