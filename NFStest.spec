Name: nfstest		
Version: 2.1.1
Release: 0.0%{?dist}
Summary: NFS Testing Tool

Group: Applications/System
License: GPLv2+ 
URL: http://wiki.linux-nfs.org/wiki/index.php/NFStest
Source0: http://www.linux-nfs.org/~mora/nfstest/releases/NFStest-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python-setuptools
BuildRequires: python2-devel
Requires: nfs-utils sudo tcpdump 

%description
Provides a set of tools for testing either the NFS client or the NFS server, 
most of the functionality is focused mainly on testing the client. 
%prep
%setup -q -n NFStest-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%{_bindir}/nfstest_cache
%{_bindir}/nfstest_delegation
%{_bindir}/nfstest_dio
%{_bindir}/nfstest_pnfs
%{_bindir}/nfstest_posix
%{_bindir}/nfstest_alloc
%{_bindir}/nfstest_file
%{_bindir}/nfstest_interop
%{_bindir}/nfstest_io
%{_bindir}/nfstest_lock
%{_bindir}/nfstest_pkt
%{_bindir}/nfstest_sparse
%{_bindir}/nfstest_xid
%{_mandir}/*/*
#For noarch packages: sitelib
%{python_sitelib}/*

%doc COPYING README

%changelog
* Thu Jan 21 2016 Steve Dickson <steved@redhat.com> 2.1.1-0.0
- Rebased to latest upstream release: 2.1.1 (bz 1284678)

* Wed Jul 23 2014 Steve Dickson <steved@redhat.com> 1.0.8-0.0
- rebuild for RHEL 7.1 (bz 1059490)

* Wed Jan 29 2014 Steve Dickson <steved@redhat.com> 1.0.8-0
- Updated to latest upstream release: 1.0.8 (bz 1059490)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.2-2
- Mass rebuild 2013-12-27

* Mon Nov  4 2013 Steve Dickson <steved@redhat.com> 1.0.2-1
- Renamed package to nfstest
- Initial RHEL-7 build (bz1026476)

* Wed Apr 24 2013 Steve Dickson <steved@redhat.com> 1.0.2-0
- Updated to latest upstream release: 1.0.2

* Mon Mar 18 2013 Steve Dickson <steved@redhat.com> 1.0.1-1
- Added required BuildRequires

* Thu Feb 21 2013 Steve Dickson <steved@redhat.com> 1.0.1-0 
- Inital commit.


