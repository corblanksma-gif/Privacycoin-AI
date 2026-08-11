#!/bin/bash
# Privacycoin AI - Clone all recommended dependencies (shallow)
# Usage: bash scripts/clone_dependencies.sh

set -e
mkdir -p dependencies
cd dependencies

echo "=== Cloning PRCY Coin ==="
git clone --depth 1 https://github.com/PRCYCoin/PRCYCoin.git || true

echo "=== Cloning PIVX ==="
git clone --depth 1 https://github.com/PIVX-Project/PIVX.git || true

echo "=== Cloning Solana (Agave) ==="
git clone --depth 1 https://github.com/anza-xyz/agave.git || true

echo "=== Cloning Aztec Packages ==="
git clone --depth 1 https://github.com/AztecProtocol/aztec-packages.git || true

echo ""
echo "Done. Repositories are in ./dependencies/"
ls -la
