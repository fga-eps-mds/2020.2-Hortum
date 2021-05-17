#!/bin/sh

python manage.py makemigrations
python manage.py migrate
./scripts/create_superuser.sh
python manage.py collectstatic --noinput --clear
python manage.py runserver 0.0.0.0:8000
