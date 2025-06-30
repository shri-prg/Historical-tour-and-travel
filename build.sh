#!/usr/bin/env bash
# filepath: c:\Users\DELL\yatraproject\yatra\build.sh

# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# (Optional) Run migrations
python manage.py migrate