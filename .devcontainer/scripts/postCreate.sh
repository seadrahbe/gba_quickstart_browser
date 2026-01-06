#!/usr/bin/env bash
set -Eeuo pipefail

echo "Beginning postCreate.sh"

echo "Initializing Butano submodule"
git submodule update --init --recursive

echo "Finished postCreate.sh"