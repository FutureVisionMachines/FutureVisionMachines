#!/bin/bash
# Render Build Script

set -e  # Exit on error

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Build completed successfully!"
