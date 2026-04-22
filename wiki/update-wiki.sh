#!/bin/bash
# Sync wiki content and push to GitHub
WIKI_DIR="/home/xing/.openclaw/workspace-tft/comp-retrieval/wiki"
QUARTZ_DIR="/tmp/tft-wiki-fresh"

cd "$QUARTZ_DIR"
rm -rf content/*
cp -r "$WIKI_DIR"/* content/
git add -A
git commit -m "wiki: update $(date +%Y-%m-%d-%H%M)" || echo "No changes"
env -u LD_PRELOAD git push origin main 2>&1
