#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting app with gunicorn..."
gunicorn --bind=0.0.0.0 --timeout 600 app:app