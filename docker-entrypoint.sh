#!/bin/bash
cd /code/ApiONG
python manage.py makemigrations
python manage.py migrate
python -u manage.py runserver 0.0.0.0:8000