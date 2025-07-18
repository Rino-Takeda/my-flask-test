#!/bin/bash

echo "Starting app with gunicorn..."
exec gunicorn --bind=0.0.0.0 --timeout 600 app:app
