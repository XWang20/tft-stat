#!/bin/bash
# TFT-Stat autonomous experiment loop
# Runs continuously: process feedback → run experiment → push → repeat
# Usage: nohup ./run-experiment.sh &

set -o pipefail
export PATH="$HOME/.local/bin:$HOME/miniconda3/bin:$PATH"
cd /home/azureuser/tft-stat

LOG_DIR="logs"
mkdir -p "$LOG_DIR"
INTERVAL=${1:-300}  # seconds between runs, default 5 min

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') $1" | tee -a "$LOG_DIR/cron.log"; }

run_cycle() {
    local TIMESTAMP=$(date +%Y%m%d-%H%M)
    local LOG_FILE="$LOG_DIR/experiment-$TIMESTAMP.log"

    log "=== cycle start ==="

    # Step 1: pull latest (in case Xing pushed changes)
    git pull --rebase 2>&1 | tee -a "$LOG_FILE"

    # Step 2: run claude (process feedback + experiment)
    local PROMPT=$(cat experiment-prompt.md)
    claude -p --dangerously-skip-permissions --max-budget-usd 5 "$PROMPT" 2>&1 | tee -a "$LOG_FILE"
    local EXIT_CODE=$?

    if [ $EXIT_CODE -ne 0 ]; then
        log "claude exited with $EXIT_CODE"
        return 1
    fi

    # Step 3: ensure push (claude might have committed but failed to push)
    if [ -n "$(git status --porcelain)" ]; then
        git add -A
        git commit -m "cron: auto-commit uncommitted changes

via [HAPI](https://hapi.run)

Co-Authored-By: HAPI <noreply@hapi.run>" 2>&1 | tee -a "$LOG_FILE"
    fi

    git push 2>&1 | tee -a "$LOG_FILE"

    # Step 4: report what happened
    local LATEST=$(git log -1 --format="%s")
    log "cycle done: $LATEST"

    return 0
}

# Main loop
log "loop started (interval: ${INTERVAL}s)"

while true; do
    run_cycle
    log "sleeping ${INTERVAL}s..."
    sleep "$INTERVAL"
done
