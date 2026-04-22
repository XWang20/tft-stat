#!/bin/bash
# Filter Design Autoresearch Loop
# Each iteration: fresh agent reads guide → designs filter → compares → updates guide
# Usage: ./run-filter-design.sh [duration_minutes] [interval_seconds]

set -o pipefail
export PATH="$HOME/.local/bin:$HOME/miniconda3/bin:$PATH"
cd /home/azureuser/tft-stat

DURATION=${1:-60}     # total minutes, default 60
INTERVAL=${2:-30}     # seconds between runs, default 30
LOG_DIR="logs"
mkdir -p "$LOG_DIR"

END_TIME=$(($(date +%s) + DURATION * 60))
ITERATION=0

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') $1" | tee -a "$LOG_DIR/filter-design.log"; }

log "=== Filter Design Autoresearch started (${DURATION}m, ${INTERVAL}s interval) ==="

while [ $(date +%s) -lt $END_TIME ]; do
    ITERATION=$((ITERATION + 1))
    TIMESTAMP=$(date +%Y%m%d-%H%M)
    ITER_LOG="$LOG_DIR/filter-design-$TIMESTAMP.log"

    log "--- iteration $ITERATION ---"

    git pull --rebase 2>&1 >> "$ITER_LOG"

    PROMPT=$(cat filter-design-prompt.md)
    claude -p --dangerously-skip-permissions --max-budget-usd 3 "$PROMPT" 2>&1 | tee -a "$ITER_LOG"

    # Ensure push
    if [ -n "$(git status --porcelain)" ]; then
        git add -A
        git commit -m "filter-design: auto-commit iteration $ITERATION

via [HAPI](https://hapi.run)

Co-Authored-By: HAPI <noreply@hapi.run>" 2>&1 >> "$ITER_LOG"
    fi
    git push 2>&1 >> "$ITER_LOG"

    LATEST=$(git log -1 --format="%s" 2>/dev/null)
    log "iteration $ITERATION done: $LATEST"

    # Check if time remaining
    REMAINING=$(( (END_TIME - $(date +%s)) / 60 ))
    log "${REMAINING}m remaining"

    if [ $(date +%s) -lt $END_TIME ]; then
        sleep "$INTERVAL"
    fi
done

log "=== Filter Design Autoresearch completed ($ITERATION iterations) ==="
