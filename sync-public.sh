#!/usr/bin/env bash
#
# Sync the public mirror from this (private) repo.
#
# The public tree is rebuilt from the private repo's committed HEAD, with every
# path marked `export-ignore` in .gitattributes (the `_files/` directories)
# filtered out by `git archive`. Deletions are handled because the public tree
# is wiped and re-extracted each run.
#
# Workflow: commit your work on the private repo, then run this script.
# `git archive` uses HEAD, so uncommitted changes are NOT synced.
#
# Usage: ./sync-public.sh [path-to-public-clone]   (default: ../chirashi-public)

set -euo pipefail

PUBLIC_DIR="${1:-../chirashi-public}"

if [ ! -d "$PUBLIC_DIR/.git" ]; then
  echo "error: no git repo at '$PUBLIC_DIR'." >&2
  echo "Clone the public repo first, e.g.:" >&2
  echo "  git clone https://github.com/ryn-cx/chirashi.git '$PUBLIC_DIR'" >&2
  exit 1
fi

REV="$(git rev-parse --short HEAD)"

# Replace the public working tree with the filtered snapshot of private HEAD.
git -C "$PUBLIC_DIR" rm -rq --ignore-unmatch . >/dev/null 2>&1 || true
git archive HEAD | tar -x -C "$PUBLIC_DIR"

# `git archive` can leave behind empty `_files/` directory entries; drop them.
find "$PUBLIC_DIR" -type d -name _files -empty -delete 2>/dev/null || true

git -C "$PUBLIC_DIR" add -A
if git -C "$PUBLIC_DIR" diff --cached --quiet; then
  echo "Public repo already up to date (private @ $REV)."
  exit 0
fi

git -C "$PUBLIC_DIR" commit -q -m "Sync from private ($REV)"
git -C "$PUBLIC_DIR" push
echo "Public repo synced to private @ $REV and pushed."
