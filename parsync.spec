%define	snap	20151217
%define	rel	1
Summary:	Parallel rsync wrapper for large data transfers
Name:		parsync
Version:	0.1
Release:	0.%{snap}.%{rel}
License:	GPL
Group:		Networking/Utilities
Source0:	http://moo.nac.uci.edu/~hjm/parsync/%{name}+utils.tar.gz
# Source0-md5:	467c0a2f5efb225d4f5d2e84edfcf005
URL:		http://moo.nac.uci.edu/~hjm/parsync/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	rsync
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
parsync is a Perl script that wraps Andrew Tridgells miraculous
'rsync' to provide some load balancing and parallel operation across
network connections to increase the amount of bandwidth it can use.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -p kdirstat-cache-writer parsync scut stats \
	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdirstat-cache-writer
%attr(755,root,root) %{_bindir}/parsync
%attr(755,root,root) %{_bindir}/scut
%attr(755,root,root) %{_bindir}/stats
