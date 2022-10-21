#!/bin/bash
# echo "Reset DB..."; python manage.py flush --no-input;
echo "Run migrate..."; python manage.py migrate;
echo "Collect static files..."; python manage.py collectstatic --no-input --clear;
echo "Running Server..."; python manage.py runserver 0.0.0.0:8000;

