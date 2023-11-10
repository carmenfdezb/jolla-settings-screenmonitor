# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       jolla-settings-screenmonitor

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    jolla-settings-screenmonitor
Version:    1.0.5
Release:    1
Group:      Applications/System
License:    GPL2
URL:        http://me.medesimo.eu
Source0:    %{name}-%{version}.tar.bz2
Source100:  jolla-settings-screenmonitor.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   nemo-qml-plugin-contextkit-qt5
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  vala

%description
A simple screen usage monitor for Sailfish OS


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%preun
# >> preun
/usr/bin/systemctl disable ScreenMonitor.service
# << preun

%post
# >> post
/usr/bin/systemctl enable ScreenMonitor.service
# << post

%files
%defattr(-,root,root,-)
%{_bindir}/ScreenMonitor
%{_sysconfdir}/dbus-1
%{_datadir}/dbus-1
%{_datadir}/jolla-settings
/lib/systemd/system
# >> files
# << files
