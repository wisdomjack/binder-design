#!/bin/bash
set -e

echo ">> Decompressing Rosetta binaries..."

gzip -dk brians_score_jd2.gz
gzip -dk extract_pdbs.gz

echo ">> Copying binaries into dl_binder_design/include/silent_tools..."

mkdir -p dl_binder_design/include/silent_tools
cp -f brians_score_jd2 dl_binder_design/include/silent_tools/
cp -f extract_pdbs dl_binder_design/include/silent_tools/

echo ">> Done."
