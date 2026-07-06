#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p ../output
python3 main.py ../input/sample_orders.csv ../output/cutting_plan_python.csv
