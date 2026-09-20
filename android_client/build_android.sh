#!/data/data/com.termux/files/usr/bin/bash

set -e

cd "$(dirname "$0")"

echo "======================================"
echo "      SKADOSH ANDROID BUILD"
echo "======================================"

echo
echo "Checking project..."

test -f main.py

echo "Android client source: OK"

echo
echo "This directory is prepared for"
echo "python-for-android / SDL2 packaging."

echo
echo "SKADOSH ANDROID CLIENT READY"
