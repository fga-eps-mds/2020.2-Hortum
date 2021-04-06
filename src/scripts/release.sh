#!/bin/sh

python manage.py makemigrations 
python manage.py migrate 
./scripts/create_superuser.sh
