#!/bin/sh

# default superuser
# email: 'admin@example.com'
# password: 'admin'

echo "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not len(User.objects.all()):
    User.objects.create_superuser(username='admin', email='admin@example.com', password='admin')" | python manage.py shell
