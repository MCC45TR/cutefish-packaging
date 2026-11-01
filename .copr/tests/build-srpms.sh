#!/usr/bin/env bash
set -euo pipefail
root=$(cd -- "$(dirname "$0")/.." && pwd)
bash -n "$root/build-srpms.sh" "$root/sync-upstream.sh"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
cp "$root/build-srpms.sh" "$tmp/"
mkdir "$tmp/referances"
if bash "$tmp/build-srpms.sh" '../outside' > "$tmp/invalid.log" 2>&1; then
    exit 1
fi
grep -q 'Unknown package:' "$tmp/invalid.log"
printf 'corrupt source\n' > "$tmp/referances/fixture.tar.gz"
checksum=$(printf 'expected source\n' | sha256sum | cut -d ' ' -f 1)
printf '%s\tfixture.tar.gz\thttps://invalid.example/unused\n' "$checksum" > "$tmp/sources.tsv"
if bash "$tmp/build-srpms.sh" > "$tmp/guard.log" 2>&1; then
    exit 1
fi
grep -q 'Checksum mismatch: fixture.tar.gz' "$tmp/guard.log"
grep -qx 'corrupt source' "$tmp/referances/fixture.tar.gz"
test -z "$(find "$tmp/build" -type f -print -quit)"
echo 'PASS: invalid selections and corrupt sources stop before source builds.'
