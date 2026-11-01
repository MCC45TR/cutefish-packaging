Name:           cutefish-suite
Version:        1.0
Release:        1%{?dist}
Summary:        Complete Cutefish desktop and application suite
License:        BSD-3-Clause
URL:            https://github.com/MCC45TR/cutefish-packaging
Source0:        BSD-3-Clause
BuildArch:      noarch
Requires:       cutefish-desktop >= 1.0^20261101
Requires:       cutefish-calculator cutefish-calendar cutefish-system-monitor
Requires:       cutefish-text-editor cutefish-video-player cutefish-qt-plugins
Requires:       cutefish-dm cutefish-plymouth-theme cutefish-computer-use

%description
Install the complete packaged Cutefish desktop, applications, Qt integration,
optional display manager, boot splash and consent-based desktop control server.
Installation does not enable the display manager, select a boot theme, start
agent control or switch the current session. Unsplash wallpapers are excluded
by COPR license policy. The Debian-only live installer is a separate package.

%prep
cp %{SOURCE0} LICENSE
%build
%install
%files
%license LICENSE

%changelog
* Sun Nov 01 2026 MCC45TR <75160848+MCC45TR@users.noreply.github.com> - 1.0-1
- Select the complete redistributable Cutefish desktop and application suite.
