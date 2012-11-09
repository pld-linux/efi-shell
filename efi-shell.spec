%define	svnrev  13902
Summary:	Native UDK implementations of a UEFI Shell 2.0
Summary(pl.UTF-8):	Natywne implementacje UDK powłoki UEFI Shell 2.0
Name:		efi-shell
Version:	2.0
Release:	0.%{svnrev}.2
License:	BSD-like
Group:		Applications
#https://edk2.svn.sourceforge.net/svnroot/edk2/trunk/edk2/ShellBinPkg
Source0:	ShellBinPkg-r%{svnrev}.tar.bz2
# Source0-md5:	00cdc30ad2e6267849be0a2b0c9901b2
Source1:	shell_ia32.efi-boot-update
Source2:	shell_x64.efi-boot-update
URL:		http://sourceforge.net/apps/mediawiki/tianocore/index.php?title=ShellPkg
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
Native UDK implementations of a UEFI Shell 2.0.

%description -l pl.UTF-8
Natywne implementacje UDK powłoki UEFI Shell 2.0.

%package ia32
Summary:	Native UDK implementation of a UEFI Shell 2.0 for IA32
Summary(pl.UTF-8):	Natywna implementacja UDK powłoki UEFI Shell 2.0 dla IA32
Group:		Base

%description ia32
32-bit version of the native UDK implementation of a UEFI Shell 2.0
(for IA32 architecture).

%description ia32 -l pl.UTF-8
32-bitowa natywna implementacja UDK powłoki UEFI Shell 2.0 (dla
architektury IA32).

%package x64
Summary:	Native UDK implementation of a UEFI Shell 2.0
Summary(pl.UTF-8):	Natywna implementacja UDK powłoki UEFI Shell 2.0 dla x64
Group:		Base

%description x64
64-bit version of the native UDK implemenations of a UEFI Shell 2.0
for x64 (x86_64) platform.

%description x64 -l pl.UTF-8
64-bitowa natywna implementacja UDK powłoki UEFI Shell 2.0 dla
architektury x64 (x86_64).

%prep
%setup -qn ShellBinPkg

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib/efi/{ia32,x64},/etc/efi-boot/update.d}
install UefiShell/Ia32/Shell.efi $RPM_BUILD_ROOT/lib/efi/ia32
install UefiShell/X64/Shell.efi $RPM_BUILD_ROOT/lib/efi/x64
install %{SOURCE1} $RPM_BUILD_ROOT/etc/efi-boot/update.d/shell_ia32.conf
install %{SOURCE2} $RPM_BUILD_ROOT/etc/efi-boot/update.d/shell_x64.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post ia32
[ -x /sbin/efi-boot-update ] && /sbin/efi-boot-update --auto || :

%postun ia32
[ -x /sbin/efi-boot-update ] && /sbin/efi-boot-update --auto || :

%post x64
[ -x /sbin/efi-boot-update ] && /sbin/efi-boot-update --auto || :

%postun x64
[ -x /sbin/efi-boot-update ] && /sbin/efi-boot-update --auto || :

%files ia32
%defattr(644,root,root,755)
%doc License.txt ReadMe.txt Contributions.txt
/lib/efi/ia32/Shell.efi
/etc/efi-boot/update.d/shell_ia32.conf

%files x64
%defattr(644,root,root,755)
%doc License.txt ReadMe.txt Contributions.txt
/lib/efi/x64/Shell.efi
/etc/efi-boot/update.d/shell_x64.conf
