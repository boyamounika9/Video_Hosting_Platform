#!/usr/bin/env bash
# build.sh — Render build script
set -o errexit  # exit on error

pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python project/manage.py collectstatic --no-input

# Run database migrations
python project/manage.py migrate
