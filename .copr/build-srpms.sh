#!/usr/bin/env bash
set -euo pipefail
root=$(cd -- "$(dirname -- "$0")" && pwd)
package=${1:-all}
[[ $package == all || $package =~ ^[a-z0-9-]+$ && -f $root/packaging/$package.spec ]] || { echo "Unknown package: $package" >&2; exit 2; }
mkdir -p "$root/referances" "$root/build/rpmbuild"/{SOURCES,SPECS,SRPMS,BUILD,RPMS,BUILDROOT}
while read -r checksum archive url; do
    [[ $checksum =~ ^[0-9a-f]{64}$ && $archive =~ ^[a-z0-9-]+\.tar\.gz$ && $url == https://* ]] || exit 1
    target=$root/referances/$archive
    if [[ ! -f $target ]]; then
        curl --fail --location --retry 3 --output "$target.part" "$url"
        printf '%s  %s\n' "$checksum" "$target.part" | sha256sum --check --status || { echo "Checksum mismatch: $archive" >&2; exit 1; }
        mv -- "$target.part" "$target"
    fi
    printf '%s  %s\n' "$checksum" "$target" | sha256sum --check --status || { echo "Checksum mismatch: $archive" >&2; exit 1; }
    cp --reflink=auto -- "$target" "$root/build/rpmbuild/SOURCES/"
done < "$root/sources.tsv"
cp -- "$root/sources.sha256" "$root/upstream.tsv" \
    "$root/packaging/cutefish-auth" "$root/packaging/cutefish-dm" \
    "$root/packaging/cutefish-dm-greeter" "$root/packaging/cutefish-greeter.conf" \
    "$root/licenses/"* "$root/patches/"* "$root/build/rpmbuild/SOURCES/"
for spec in "$root/packaging/"*.spec; do
    [[ $package == all || ${spec##*/} == "$package.spec" ]] || continue
    cp -- "$spec" "$root/build/rpmbuild/SPECS/"
    rpmbuild -bs --target aarch64 --define "_topdir $root/build/rpmbuild" \
        --define '_buildhost localhost' --define 'dist .fc46' "$spec"
done
