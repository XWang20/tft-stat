#!/bin/bash
# TFT-Stat daily experiment runner
# Called by crontab 3x daily

export PATH="$HOME/.local/bin:$HOME/miniconda3/bin:$PATH"
cd /home/azureuser/tft-stat

LOG_DIR="logs"
mkdir -p "$LOG_DIR"
TIMESTAMP=$(date +%Y%m%d-%H%M)
LOG_FILE="$LOG_DIR/experiment-$TIMESTAMP.log"

echo "$(date): starting experiment" >> "$LOG_DIR/cron.log"

PROMPT=$(cat experiment-prompt.md)
claude -p --dangerously-skip-permissions --max-budget-usd 5 "$PROMPT" 2>&1 | tee "$LOG_FILE"

echo "$(date): experiment completed (exit $?), log at $LOG_FILE" >> "$LOG_DIR/cron.log"
