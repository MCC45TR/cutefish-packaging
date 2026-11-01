# Fedora Cutefish packaging

2026-11-01. Fedora 44, Fedora 45 and Rawhide, AArch64 only.
The expanded native COPR builds are in progress. No installation, graphical
session, image or physical-device acceptance is claimed.

This fork preserves [Cutefish upstream](https://github.com/cutefishos/packaging)
history, names, copyright and licenses. Fedora recipes and reviewed patches
live in `.copr/`; desktop sources remain in individual upstream forks listed
in `forks.tsv`. `upstream.tsv` pins every revision and `sources.tsv` records
archive URLs and SHA-256 checksums. Sources are built from these forks.

`cutefish-desktop` retains the existing nine-component desktop bundle and its
development subpackage. Additional RPMs provide Calculator, Calendar and
reminders, System Monitor, Text Editor, Video Player, Qt 6 integration, the
optional display manager, Plymouth themes and the consent-based computer-use
server. `cutefish-suite` selects all these runtime components.

The upstream Unsplash wallpapers are excluded from SRPMs and RPMs under
[COPR license policy](https://docs.copr.fedorainfracloud.org/user_documentation.html#what-i-can-build-in-copr).
The compositor retains its solid-color fallback. The separate experimental
`cutefish-installer` package builds the Debian live installer; its privileged
service refuses Fedora before registering on D-Bus. It has no autostart entry,
is hidden from the application menu and is excluded from the desktop meta
package. Its APT/DPKG and boot-loader operations are not a Fedora installer.

Install the whole desktop on a supported Fedora AArch64 system:

```sh
sudo dnf copr enable mcc45tr/cutefish
sudo dnf install cutefish-suite
```

Keep normal Fedora release and updates repositories enabled. Installation
does not switch the session, replace or enable a display manager, select a
Plymouth theme, configure an agent or grant desktop-control consent.
Select **Cutefish (Wayland)** in the existing login manager. Authentication,
locale setup, graphical sessions and physical-device operation remain
separate validation requirements. These commands were not run on the host.

Prepare sources with Fedora `rpm-build`, `redhat-rpm-config`, `curl` and `tar`:

```sh
bash .copr/tests/contract.sh
bash .copr/tests/build-srpms.sh
bash .copr/tests/sync-upstream.sh
bash .copr/build-srpms.sh
```

Pass a source package name to prepare only that SRPM. COPR source jobs fetch
this fork and use the same helper. Binary builds have networking disabled.
Fedora supplies native GN, libraries and Rust crates. Unmodified Skia GN
helpers execute Python only inside the build host, at Skia commit
`95ee33d7ec7791ab9c071675710a14fe6408ae4f`; replacing its maintained build
generator has no practical packaging alternative. No Python source, bytecode
or entrypoint is installed by these RPMs. Original Fedora dependencies retain
their distribution-provided helpers.

Daily upstream synchronization merges each original repository into its fork,
preserves downstream commits and aborts conflicts without pushing. Package
sources remain pinned; upstream synchronization does not automatically
publish untested revisions. Changes to a pin require new checksums, review,
COPR builds and package/dependency validation before promotion.
