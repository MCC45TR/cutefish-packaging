%global commit fac87113b59cd5e5b067e11de48163aa24e4a9bf
Name:           cutefish-computer-use
Version:        1.0.0
Release:        3%{?dist}
Summary:        Consent-based Cutefish desktop control for agent applications
License:        BSD-3-Clause AND MIT AND Apache-2.0 AND (Apache-2.0 WITH LLVM-exception) AND Unicode-3.0
URL:            https://github.com/cutefishos/cutefish-computer-use
Source0:        https://codeload.github.com/MCC45TR/cutefish-computer-use/tar.gz/%{commit}#/cutefish-computer-use-%{commit}.tar.gz
ExclusiveArch:  aarch64
BuildRequires:  rust cargo
BuildRequires:  cargo-rpm-macros jq
BuildRequires:  (crate(base64/default) >= 0.22 with crate(base64/default) < 0.23)
BuildRequires:  rust-bitflags+default-devel
BuildRequires:  rust-jpeg-encoder+default-devel rust-libc+default-devel
BuildRequires:  rust-memmap2+default-devel rust-serde_json+default-devel
BuildRequires:  (crate(png/default) >= 0.17 with crate(png/default) < 0.18)
BuildRequires:  rust-wayland-backend+default-devel rust-wayland-client+default-devel
BuildRequires:  rust-wayland-protocols+client-devel rust-wayland-protocols+staging-devel
BuildRequires:  rust-wayland-protocols+unstable-devel rust-wayland-scanner+default-devel
BuildRequires:  pkgconfig(wayland-client)
Requires:       cutefish-desktop >= 1.0^20261101

%description
The upstream MCP server for Cutefish desktop capture, pointer and keyboard
control. The compositor requests user consent. This package does not enable a
service, configure an agent, or grant consent during installation.

%prep
%autosetup -n cutefish-computer-use-%{commit}
# Fedora Rawhide carries jpeg-encoder 0.7; stable Fedora also accepts 0.6.
sed -i 's/jpeg-encoder = "0.6"/jpeg-encoder = ">=0.6, <0.8"/' Cargo.toml

%build
%set_build_flags
cargo build --release --offline
%cargo_license_summary
%cargo_license > LICENSE.dependencies
cargo metadata --offline --format-version 1 > cargo-metadata.json

%install
install -Dm755 target/release/cutefish-computer-use %{buildroot}%{_bindir}/cutefish-computer-use
jq -r '.packages[] | [.name, .version, (.manifest_path | sub("/Cargo.toml$"; ""))] | @tsv' cargo-metadata.json |
while IFS="$(printf '\t')" read -r crate version directory; do
    [ "$crate" != cutefish-computer-use ] || continue
    for notice in "$directory"/LICENSE* "$directory"/COPYING* "$directory"/NOTICE* "$directory"/COPYRIGHT*; do
        [ -f "$notice" ] || continue
        install -Dm644 "$notice" "%{buildroot}%{_licensedir}/%{name}/dependencies/$crate-$version/${notice##*/}"
    done
done

%check
cargo test --release --offline
test -z "$(find %{buildroot} -type f \( -name '*.py' -o -name '*.pyc' \) -print -quit)"

%files
%license LICENSE LICENSE.dependencies
%license %{_licensedir}/%{name}/dependencies/
%doc README.md Cargo.lock
%{_bindir}/cutefish-computer-use

%changelog
* Sun Nov 01 2026 MCC45TR <75160848+MCC45TR@users.noreply.github.com> - 1.0.0-3
- Retain statically linked crate notices, exact dependency versions and licenses.

* Sun Nov 01 2026 MCC45TR <75160848+MCC45TR@users.noreply.github.com> - 1.0.0-2
- Select the Fedora base64 compatibility crate matching the upstream API.

* Sun Nov 01 2026 MCC45TR <75160848+MCC45TR@users.noreply.github.com> - 1.0.0-1
- Build offline against Fedora Rust crates without enabling desktop control.
