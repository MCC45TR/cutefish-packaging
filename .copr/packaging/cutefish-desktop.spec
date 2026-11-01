Name:           cutefish-desktop
Version:        1.0^20261101
Release:        5%{?dist}
Summary:        Upstream Cutefish Wayland desktop
License:        BSD-3-Clause AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-or-later AND MIT
URL:            https://cutefish.org/
ExclusiveArch:  aarch64

Source0: https://codeload.github.com/MCC45TR/cutefish-toolkit/tar.gz/9578923b4e30c58f78ef548122782d6a11e5eb85#/cutefish-toolkit-9578923b4e30c58f78ef548122782d6a11e5eb85.tar.gz
Source1: https://codeload.github.com/MCC45TR/cutefish-framework/tar.gz/dc479f9a40bc82be4da6a395be44a4f5141487ba#/cutefish-framework-dc479f9a40bc82be4da6a395be44a4f5141487ba.tar.gz
Source2: https://codeload.github.com/MCC45TR/cutefish-core/tar.gz/1aa0ac9cda0f4b46c69cb74f9444712f3279b6b1#/cutefish-core-1aa0ac9cda0f4b46c69cb74f9444712f3279b6b1.tar.gz
Source3: https://codeload.github.com/MCC45TR/cutefish-compositor/tar.gz/3abce3799c6e8251609b020b45676a3d0d5c6c5e#/cutefish-compositor-3abce3799c6e8251609b020b45676a3d0d5c6c5e.tar.gz
Source4: https://codeload.github.com/MCC45TR/cutefish-filemanager/tar.gz/ccde0c5722b0cc3031251c6da0349a2234991fb0#/filemanager-ccde0c5722b0cc3031251c6da0349a2234991fb0.tar.gz
Source5: https://codeload.github.com/MCC45TR/cutefish-icons/tar.gz/a38be51fe7f6a87a9b2bb4928f8d96134a066848#/icons-a38be51fe7f6a87a9b2bb4928f8d96134a066848.tar.gz
Source6: https://codeload.github.com/MCC45TR/cutefish-settings/tar.gz/a3cdcfa95e81c4bf96ee4fbaf9ec6228a3e7f70c#/settings-a3cdcfa95e81c4bf96ee4fbaf9ec6228a3e7f70c.tar.gz
Source7: https://codeload.github.com/MCC45TR/cutefish-terminal/tar.gz/7bdca050de4c9dcf4f2230df9cf6a048c23f4d5a#/terminal-7bdca050de4c9dcf4f2230df9cf6a048c23f4d5a.tar.gz
Source8: https://codeload.github.com/MCC45TR/xdg-desktop-portal-cutefish/tar.gz/03d019c0bf5cb875881f852b6a74e2b1670a5949#/xdg-desktop-portal-cutefish-03d019c0bf5cb875881f852b6a74e2b1670a5949.tar.gz
Source9: https://codeload.github.com/MCC45TR/cutefish-calculator/tar.gz/7994fab9ca65098305c7d1e5b2f0affcd7d9189e#/calculator-7994fab9ca65098305c7d1e5b2f0affcd7d9189e.tar.gz
Source10: https://codeload.github.com/MCC45TR/cutefish-calendar/tar.gz/5a0572f24fac450181ac7e6fc1d7f4106a365976#/calendar-5a0572f24fac450181ac7e6fc1d7f4106a365976.tar.gz
Source11: https://codeload.github.com/MCC45TR/cutefish-dm/tar.gz/77e122903da3d8a1afbd80a9f240b0f318539b17#/cutefish-dm-77e122903da3d8a1afbd80a9f240b0f318539b17.tar.gz
Source12: https://codeload.github.com/MCC45TR/cutefish-installer/tar.gz/0cb8ef507f7be0f3dc26ce56d0a168f9210881a5#/cutefish-installer-0cb8ef507f7be0f3dc26ce56d0a168f9210881a5.tar.gz
Source13: https://codeload.github.com/MCC45TR/cutefish-plymouth-theme/tar.gz/8fbc39b1dac39192d8c21ae9ca876f1b528adeaf#/plymouth-theme-8fbc39b1dac39192d8c21ae9ca876f1b528adeaf.tar.gz
Source14: https://codeload.github.com/MCC45TR/cutefish-qt-plugins/tar.gz/8d79992d37764b6e487b7e7a16c83eab6f4b69ee#/qt-plugins-8d79992d37764b6e487b7e7a16c83eab6f4b69ee.tar.gz
Source15: https://codeload.github.com/MCC45TR/cutefish-system-monitor/tar.gz/c09b8eae8dc53bbfc57ad043a914e201ee6aa4fa#/system-monitor-c09b8eae8dc53bbfc57ad043a914e201ee6aa4fa.tar.gz
Source16: https://codeload.github.com/MCC45TR/cutefish-text-editor/tar.gz/2a4b93d16332aa6806330e18b183011636b27e10#/text-editor-2a4b93d16332aa6806330e18b183011636b27e10.tar.gz
Source17: https://codeload.github.com/MCC45TR/cutefish-video-player/tar.gz/0037aa0a58a3fe3816adf99ca96b27678a330ea2#/video-player-0037aa0a58a3fe3816adf99ca96b27678a330ea2.tar.gz
Source18: https://codeload.github.com/google/skia/tar.gz/95ee33d7ec7791ab9c071675710a14fe6408ae4f#/skia-95ee33d7ec7791ab9c071675710a14fe6408ae4f.tar.gz
Source19: sources.sha256
Source20: upstream.tsv
Source21: cutefish-auth
Source22: cutefish-dm
Source23: cutefish-dm-greeter
Source24: cutefish-greeter.conf
Source25: BSD-3-Clause
Source26: GPL-3.0
Patch0: installer-debian-only.patch
Patch1: qt-theme-notification.patch

BuildRequires: gcc-c++ clang cmake ninja-build gn python3 gettext binutils
BuildRequires: pkgconfig(mpv) pkgconfig(libical) pkgconfig(libcurl)
BuildRequires: qt6-qtbase-devel qt6-qtbase-private-devel
BuildRequires: qt6-qtdeclarative-devel qt6-qtdeclarative-private-devel
BuildRequires: librsvg2-devel gtest-devel systemd-rpm-macros
BuildRequires: pkgconfig desktop-file-utils
BuildRequires: wayland-devel >= 1.23
BuildRequires: wayland-protocols-devel >= 1.39
BuildRequires: mesa-libEGL-devel mesa-libGLES-devel mesa-libgbm-devel
BuildRequires: libdrm-devel libxkbcommon-devel libinput-devel libseat-devel
BuildRequires: systemd-devel pam-devel fontconfig-devel freetype-devel
BuildRequires: harfbuzz-devel libicu-devel expat-devel libpng-devel
BuildRequires: libjpeg-turbo-devel zlib-ng-compat-devel libwebp-devel
BuildRequires: libtiff-devel libheif-devel libjxl-devel
BuildRequires: pipewire-devel ffmpeg-free-devel libva-devel libxcb-devel
BuildRequires: libarchive-devel fuse3-devel libmtp-devel libsmbclient-devel
BuildRequires: libssh-devel libzip-devel libxcrypt-devel libXcursor-devel
BuildRequires: pcre2-devel gtk-update-icon-cache
BuildRequires: bzip2-devel xz-devel lzfse-devel

Provides: bundled(skia) = 156
Requires: accountsservice polkit gsettings-desktop-schemas xdg-user-dirs
Requires: NetworkManager bluez upower power-profiles-daemon udisks2 fuse3
Requires: pipewire pipewire-pulseaudio wireplumber gnome-keyring gnome-keyring-pam
Requires: xdg-desktop-portal xorg-x11-server-Xwayland adwaita-icon-theme
Requires: glibc-locale-source glibc-langpack-en

%description
The upstream Cutefish desktop, built for Fedora Rawhide AArch64. Includes its
toolkit, service framework, session, compositor, file manager, icons, Settings,
Terminal and desktop portal. Cutefish source and branding belong to upstream.
This package supplies Fedora packaging only. It does not replace or enable a
display manager, select a default session, or install Uke hardware support.
Unsplash wallpapers are excluded by COPR policy. Optional desktop applications
and integrations are available as subpackages. The Debian live installer
is experimental and refuses non-Debian systems before starting its service.

%package devel
Summary: Development files for the upstream Cutefish toolkit and framework
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig(libpipewire-0.3) >= 0.3.65

%description devel
Headers, linker names and CMake packages for the upstream Cutefish libraries.

%package -n cutefish-calculator
Summary: Calculator for Cutefish
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n cutefish-calculator
Calculator from the pinned upstream Cutefish source.

%package -n cutefish-calendar
Summary: Calendar and reminders for Cutefish
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n cutefish-calendar
Calendar and reminders from the pinned upstream Cutefish source.

%package -n cutefish-dm
Summary: Optional display manager for Cutefish
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: systemd pam gnome-keyring-pam
Requires(pre): /usr/bin/systemd-sysusers

%description -n cutefish-dm
Optional display manager from the pinned upstream Cutefish source.
Installation does not enable or replace the existing display manager.

%package -n cutefish-installer
Summary: Experimental Debian-only live installer for Cutefish
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n cutefish-installer
Experimental Debian-only live installer from the pinned upstream Cutefish source.
The upstream installer uses APT/DPKG and Debian boot-loader operations.
Its privileged service refuses Fedora before registering on D-Bus.
This package is excluded from cutefish-suite and is not a Fedora installer.

%package -n cutefish-qt-plugins
Summary: Qt 6 platform, scrolling and image integration for Cutefish
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n cutefish-qt-plugins
Qt 6 platform, scrolling and image integration from the pinned upstream Cutefish source.

%package -n cutefish-system-monitor
Summary: System monitor for Cutefish
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n cutefish-system-monitor
System monitor from the pinned upstream Cutefish source.

%package -n cutefish-text-editor
Summary: Text editor for Cutefish
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n cutefish-text-editor
Text editor from the pinned upstream Cutefish source.

%package -n cutefish-video-player
Summary: Video player for Cutefish
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n cutefish-video-player
Video player from the pinned upstream Cutefish source.

%package -n cutefish-plymouth-theme
Summary: Optional boot splash theme for Cutefish
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildArch: noarch
Requires: plymouth plymouth-plugin-script
License: GPL-3.0-only AND GPL-2.0-or-later

%description -n cutefish-plymouth-theme
Optional boot splash theme from the pinned upstream Cutefish source.

%prep
%setup -q -c -T
(cd %{_sourcedir} && sha256sum -c %{SOURCE19})
mkdir cutefish-toolkit
tar -xf %{SOURCE0} --strip-components=1 -C cutefish-toolkit
mkdir cutefish-framework
tar -xf %{SOURCE1} --strip-components=1 -C cutefish-framework
mkdir cutefish-core
tar -xf %{SOURCE2} --strip-components=1 -C cutefish-core
mkdir cutefish-compositor
tar -xf %{SOURCE3} --strip-components=1 -C cutefish-compositor
mkdir filemanager
tar -xf %{SOURCE4} --strip-components=1 -C filemanager
mkdir icons
tar -xf %{SOURCE5} --strip-components=1 -C icons
mkdir settings
tar -xf %{SOURCE6} --strip-components=1 -C settings
mkdir terminal
tar -xf %{SOURCE7} --strip-components=1 -C terminal
mkdir xdg-desktop-portal-cutefish
tar -xf %{SOURCE8} --strip-components=1 -C xdg-desktop-portal-cutefish
mkdir calculator
tar -xf %{SOURCE9} --strip-components=1 -C calculator
mkdir calendar
tar -xf %{SOURCE10} --strip-components=1 -C calendar
mkdir cutefish-dm
tar -xf %{SOURCE11} --strip-components=1 -C cutefish-dm
mkdir cutefish-installer
tar -xf %{SOURCE12} --strip-components=1 -C cutefish-installer
mkdir plymouth-theme
tar -xf %{SOURCE13} --strip-components=1 -C plymouth-theme
mkdir qt-plugins
tar -xf %{SOURCE14} --strip-components=1 -C qt-plugins
mkdir system-monitor
tar -xf %{SOURCE15} --strip-components=1 -C system-monitor
mkdir text-editor
tar -xf %{SOURCE16} --strip-components=1 -C text-editor
mkdir video-player
tar -xf %{SOURCE17} --strip-components=1 -C video-player
mkdir -p cutefish-toolkit/third_party/skia
tar -xf %{SOURCE18} --strip-components=1 -C cutefish-toolkit/third_party/skia
# Use Fedora's native GN; no downloaded build executable or network fetch.
ln -s %{_bindir}/gn cutefish-toolkit/third_party/skia/bin/gn

%patch -P 0 -p1
%patch -P 1 -p1

%build
%set_build_flags
stage=$PWD/stage
export CMAKE_PREFIX_PATH="$stage%{_prefix}"
export LD_LIBRARY_PATH="$stage%{_libdir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
for component in cutefish-toolkit cutefish-framework qt-plugins icons cutefish-core cutefish-dm filemanager terminal xdg-desktop-portal-cutefish settings calculator system-monitor text-editor video-player calendar cutefish-installer cutefish-compositor; do
    tests=OFF
    [ "$component" != calculator ] || tests=ON
    cmake -S "$component" -B "build/$component" -G Ninja \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_INSTALL_LIBDIR=%{_lib} \
        -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} \
        -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBUILD_TESTING="$tests"
    cmake --build "build/$component" --parallel %{_smp_build_ncpus}
    DESTDIR="$stage" cmake --install "build/$component"
done

%install
cp -a stage/. %{buildroot}/
# Debian common-auth/common-account have no Fedora provider.
install -m644 %{SOURCE21} %{buildroot}%{_sysconfdir}/pam.d/cutefish-auth
mkdir -p %{buildroot}%{_licensedir}/%{name} %{buildroot}%{_docdir}/%{name}
for component in cutefish-toolkit cutefish-framework cutefish-core cutefish-compositor filemanager icons settings terminal xdg-desktop-portal-cutefish; do
    install -Dm644 "$component/LICENSE" "%{buildroot}%{_licensedir}/%{name}/$component/LICENSE"
done
install -Dm644 cutefish-toolkit/third_party/skia/LICENSE %{buildroot}%{_licensedir}/%{name}/skia/LICENSE
install -Dm644 cutefish-toolkit/third_party/skia/modules/skcms/LICENSE %{buildroot}%{_licensedir}/%{name}/skcms/LICENSE
install -Dm644 terminal/qmltermwidget/LICENSE %{buildroot}%{_licensedir}/%{name}/qmltermwidget/LICENSE
install -m644 terminal/qmltermwidget/LICENSE.BSD-3-clause terminal/qmltermwidget/LICENSE.LGPL2+ %{buildroot}%{_licensedir}/%{name}/qmltermwidget/
install -m644 %{SOURCE19} %{SOURCE20} %{buildroot}%{_docdir}/%{name}/
for component in calculator calendar cutefish-dm cutefish-installer qt-plugins system-monitor text-editor video-player; do
    case "$component" in cutefish-*) package=$component;; *) package=cutefish-$component;; esac
    install -Dm644 "$component/LICENSE" "%{buildroot}%{_licensedir}/$package/LICENSE"
done
install -m644 %{SOURCE22} %{buildroot}%{_sysconfdir}/pam.d/cutefish-dm
install -m644 %{SOURCE23} %{buildroot}%{_sysconfdir}/pam.d/cutefish-dm-greeter
install -Dm644 %{SOURCE24} %{buildroot}%{_sysusersdir}/cutefish-greeter.conf
install -d -m700 %{buildroot}%{_localstatedir}/lib/cutefish-greeter
mkdir -p %{buildroot}%{_datadir}/plymouth/themes
cp -a plymouth-theme/cutefish-logo plymouth-theme/cutefish-text %{buildroot}%{_datadir}/plymouth/themes/
rm -f %{buildroot}%{_datadir}/plymouth/themes/cutefish-text/*.in
install -Dm644 %{SOURCE26} %{buildroot}%{_licensedir}/cutefish-plymouth-theme/COPYING
# A Debian live installer must not autostart on an installed Fedora desktop.
rm %{buildroot}%{_sysconfdir}/xdg/autostart/cutefish-installer.desktop
printf '\nNoDisplay=true\n' >> %{buildroot}%{_datadir}/applications/cutefish-installer.desktop
%find_lang %{name} --all-name

%check
build/calculator/tests/calculator-engine-tests
# Verify the privileged installer rejects Fedora before opening the system bus.
set +e
LD_LIBRARY_PATH="$PWD/stage%{_libdir}" %{buildroot}%{_libexecdir}/cutefish-installer-service > installer-guard.log 2>&1
status=$?
set -e
test "$status" -eq 77
grep -F 'Fedora installation is unsupported' installer-guard.log
test -x %{buildroot}%{_bindir}/cutefish-compositor
test -x %{buildroot}%{_bindir}/cutefish-wayland-session
test -x %{buildroot}%{_bindir}/cutefish-settings
test -x %{buildroot}%{_bindir}/cutefish-terminal
test -x %{buildroot}%{_bindir}/cutefish-filemanager
# DesktopNames is a display-manager session key, outside the application spec.
grep -Fx 'DesktopNames=Cutefish;' %{buildroot}%{_datadir}/wayland-sessions/cutefish-wayland.desktop
sed '/^DesktopNames=/d' %{buildroot}%{_datadir}/wayland-sessions/cutefish-wayland.desktop > session-check.desktop
desktop-file-validate session-check.desktop
! grep -E 'common-auth|common-account' %{buildroot}%{_sysconfdir}/pam.d/cutefish-auth || exit 1
find %{buildroot} -type f \( -name '*.py' -o -name '*.pyc' -o -name '*.pyo' \) > python-files.txt
test ! -s python-files.txt
! grep -rlE '^#!.*python' %{buildroot} || exit 1
find %{buildroot} -type f -exec file --brief {} + > payload-types.txt
! grep -i 'python' payload-types.txt || exit 1
find %{buildroot}%{_libdir} -name '*.a' > static-libraries.txt
test ! -s static-libraries.txt
test ! -d %{buildroot}%{_datadir}/backgrounds/cutefishos
# Imported build dependencies must not escape into installed CMake metadata.
! grep -rF "$PWD/stage" %{buildroot}%{_libdir}/cmake || exit 1

%files -f %{name}.lang
%license %{_licensedir}/%{name}/
%license %{_licensedir}/cutefish-compositor/
%doc %{_docdir}/%{name}/
%{_bindir}/cutefish-*
%{_libexecdir}/cutefish-*
%{_libexecdir}/xdg-desktop-portal-cutefish
%{_libdir}/libcutefish-*.so.*
%{_datadir}/applications/*cutefish*.desktop
%{_datadir}/cutefish*/
%{_datadir}/icons/Cutefish/
%{_datadir}/wayland-sessions/cutefish-wayland.desktop
%{_datadir}/dbus-1/services/*cutefish*
%{_datadir}/dbus-1/system-services/*cutefish*
%{_datadir}/dbus-1/system.d/*cutefish*
%{_datadir}/polkit-1/actions/*cutefish*
%{_datadir}/polkit-1/rules.d/*cutefish*
%{_datadir}/xdg-desktop-portal/*cutefish*
%{_datadir}/xdg-desktop-portal/portals/cutefish.portal
%{_prefix}/lib/systemd/system/cutefish-*.service
%{_prefix}/lib/systemd/user/*cutefish*
%{_prefix}/lib/systemd/user/xdg-document-portal.service.d/
%{_prefix}/lib/udev/rules.d/*cutefish*
%{_prefix}/lib/modules-load.d/cutefish-ddc.conf
%config(noreplace) %{_sysconfdir}/pam.d/cutefish-auth
%config(noreplace) %{_sysconfdir}/fonts/conf.d/56-cutefish-sans.conf

%exclude %{_bindir}/cutefish-calculator
%exclude %{_datadir}/applications/cutefish-calculator.desktop
%exclude %{_bindir}/cutefish-calendar*
%exclude %{_datadir}/applications/cutefish-calendar.desktop
%exclude %{_bindir}/cutefish-dm
%exclude %{_libexecdir}/cutefish-dm-*
%exclude %{_datadir}/dbus-1/system.d/org.cutefish.DisplayManager.conf
%exclude %{_unitdir}/cutefish-dm.service
%exclude %{_bindir}/cutefish-installer
%exclude %{_libexecdir}/cutefish-installer-service
%exclude %{_datadir}/cutefish-installer/
%exclude %{_datadir}/applications/cutefish-installer.desktop
%exclude %{_datadir}/dbus-1/system.d/org.cutefish.Installer.conf
%exclude %{_datadir}/dbus-1/system-services/org.cutefish.Installer.service
%exclude %{_datadir}/polkit-1/actions/org.cutefish.installer.policy
%exclude %{_unitdir}/cutefish-installer.service
%exclude %{_bindir}/cutefish-system-monitor
%exclude %{_datadir}/applications/cutefish-system-monitor.desktop
%exclude %{_bindir}/cutefish-text-editor
%exclude %{_datadir}/applications/cutefish-text-editor.desktop
%exclude %{_bindir}/cutefish-video-player
%exclude %{_datadir}/applications/cutefish-video-player.desktop

%files devel
%{_includedir}/cutefish*/
%{_libdir}/cmake/Cutefish*/
%{_libdir}/libcutefish-*.so
%exclude %{_libdir}/libcutefish-qt-scrolling*.so

%files -n cutefish-calculator
%license %{_licensedir}/cutefish-calculator/
%{_bindir}/cutefish-calculator
%{_datadir}/applications/cutefish-calculator.desktop

%files -n cutefish-calendar
%license %{_licensedir}/cutefish-calendar/
%{_bindir}/cutefish-calendar*
%{_datadir}/applications/cutefish-calendar.desktop
%{_sysconfdir}/xdg/autostart/cutefish-calendar-reminders.desktop

%files -n cutefish-dm
%license %{_licensedir}/cutefish-dm/
%{_bindir}/cutefish-dm
%{_libexecdir}/cutefish-dm-*
%config(noreplace) %{_sysconfdir}/pam.d/cutefish-dm*
%{_datadir}/dbus-1/system.d/org.cutefish.DisplayManager.conf
%{_unitdir}/cutefish-dm.service
%{_userunitdir}/pipewire*.d/cutefish-dm.conf
%{_userunitdir}/wireplumber.service.d/cutefish-dm.conf
%{_userunitdir}/filter-chain.service.d/cutefish-dm.conf
%{_sysusersdir}/cutefish-greeter.conf
%attr(0700,cutefish-greeter,cutefish-greeter) %dir %{_localstatedir}/lib/cutefish-greeter

%files -n cutefish-installer
%license %{_licensedir}/cutefish-installer/
%{_bindir}/cutefish-installer
%{_libexecdir}/cutefish-installer-service
%{_datadir}/cutefish-installer/
%{_datadir}/applications/cutefish-installer.desktop
%{_datadir}/dbus-1/system.d/org.cutefish.Installer.conf
%{_datadir}/dbus-1/system-services/org.cutefish.Installer.service
%{_datadir}/polkit-1/actions/org.cutefish.installer.policy
%{_unitdir}/cutefish-installer.service

%files -n cutefish-qt-plugins
%license %{_licensedir}/cutefish-qt-plugins/
%{_libdir}/qt6/plugins/platformthemes/libcutefishplatformtheme.so
%{_libdir}/qt6/plugins/imageformats/*
%{_libdir}/libcutefish-qt-scrolling*.so

%files -n cutefish-system-monitor
%license %{_licensedir}/cutefish-system-monitor/
%{_bindir}/cutefish-system-monitor
%{_datadir}/applications/cutefish-system-monitor.desktop

%files -n cutefish-text-editor
%license %{_licensedir}/cutefish-text-editor/
%{_bindir}/cutefish-text-editor
%{_datadir}/applications/cutefish-text-editor.desktop

%files -n cutefish-video-player
%license %{_licensedir}/cutefish-video-player/
%{_bindir}/cutefish-video-player
%{_datadir}/applications/cutefish-video-player.desktop

%files -n cutefish-plymouth-theme
%license %{_licensedir}/cutefish-plymouth-theme/
%{_datadir}/plymouth/themes/cutefish-logo/
%{_datadir}/plymouth/themes/cutefish-text/

%pre -n cutefish-dm
systemd-sysusers - <<'EOF'
u cutefish-greeter - "Cutefish display manager" /var/lib/cutefish-greeter /usr/sbin/nologin
EOF

%changelog
* Sun Nov 01 2026 MCC45TR <75160848+MCC45TR@users.noreply.github.com> - 1.0^20261101-5
- Own the upstream Cutefish font-family alias configuration.

* Sun Nov 01 2026 MCC45TR <75160848+MCC45TR@users.noreply.github.com> - 1.0^20261101-4
- Own the greeter home directory with its dedicated account and private permissions.

* Sun Nov 01 2026 MCC45TR <75160848+MCC45TR@users.noreply.github.com> - 1.0^20261101-3
- Use the global Qt theme notification supported by Fedora's Qt versions.

* Sun Nov 01 2026 MCC45TR <75160848+MCC45TR@users.noreply.github.com> - 1.0^20261101-2
- Use the byte-stable GitHub Skia mirror archive for reproducible source jobs.

* Sun Nov 01 2026 MCC45TR <75160848+MCC45TR@users.noreply.github.com> - 1.0^20261101-1
- Build the complete redistributable upstream desktop and optional components.
- Preserve the existing display manager and refuse the Debian installer on Fedora.

* Tue Oct 27 2026 MCC45TR <MCC45TR@users.noreply.github.com> - 1.0^20261101-4
- Require PipeWire development files for the public audio client headers.
- Match actual upstream installation paths and make payload checks enforce failures.

* Tue Oct 27 2026 MCC45TR <MCC45TR@users.noreply.github.com> - 1.0^20261101-3
- Validate the session extension separately while preserving its upstream bytes.

* Tue Oct 27 2026 MCC45TR <MCC45TR@users.noreply.github.com> - 1.0^20261101-2
- Declare the file manager archive dependencies and preserve terminal notices.

* Tue Oct 27 2026 MCC45TR <MCC45TR@users.noreply.github.com> - 1.0^20261101-1
- Package the pinned upstream Wayland desktop for Rawhide AArch64.
- Use Fedora GN and PAM; exclude Unsplash wallpapers and optional agent tools.
