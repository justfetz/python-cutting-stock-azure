#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p out
javac -d out src/cs/*.java tests/TestCuttingStock.java
java -cp out cs.tests.TestCuttingStock
