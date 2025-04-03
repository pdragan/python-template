#!/bin/bash

echo "Setting up the environment..."
uv venv

echo "Activating the virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
uv sync

echo "Ready to go!"