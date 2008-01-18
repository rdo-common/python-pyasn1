%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define module pyasn1

Name:           python-pyasn1
Version:        0.0.7a
Release:        4%{?dist}
Summary:        ASN.1 tools for Python
License:        BSD
Group:          System Environment/Libraries
Source0:        http://downloads.sourceforge.net/pyasn1/pyasn1-%{version}.tar.gz
URL:            http://pyasn1.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools

%description
This project is dedicated to implementation of ASN.1 types (concrete syntax)
and codecs (transfer syntaxes) for Python programming environment. ASN.1
compiler is planned for implementation in the future.


%prep
%setup -n %{module}-%{version} -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README LICENSE examples/*
%{python_sitelib}/*


%changelog
* Wed Jan 16 2008 Rob Crittenden <rcritten@redhat.com> - 0.0.7a-4
- Use setuptools to install the package
- simplify the files included in the rpm so it includes the .egg-info

* Mon Jan 14 2008 Rob Crittenden <rcritten@redhat.com> - 0.0.7a-3
- Rename to python-pyasn1
- Spec file cleanups

* Mon Nov 19 2007 Karl MacMillan <kmacmill@redhat.com> - 0.0.7a-2
- Update rpm to be more fedora friendly

* Thu Nov 8 2007 Simo Sorce <ssorce@redhat.com> 0.0.7a-1
- New release

* Mon May 28 2007 Andreas Hasenack <andreas@mandriva.com> 0.0.6a-1mdv2008.0
+ Revision: 31989
- fixed (build)requires
- Import pyasn1

