#!/bin/zsh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
LOG_DIR="$PROJECT_DIR/results/reversal_3_2_live"

mkdir -p "$LOG_DIR"

cd "$PROJECT_DIR"
"$PYTHON_BIN" reversal_3_2_live.py "$@" >> "$LOG_DIR/runner.log" 2>> "$LOG_DIR/runner.err.log"
