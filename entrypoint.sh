#!/bin/sh

echo "Waiting for database..."

# Wait db be available
while ! nc -z db 5432; do
  sleep 1
done

echo "Database is up!"

# Apply migrations
python src/manage.py migrate

# Create superuser
python src/manage.py shell <<EOF
from django.contrib.auth.models import User
import os

username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin")
email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print(f"Superuser {username} created successfully.")
else:
    print(f"Superuser {username} already exists.")
EOF

# Start server
python src/manage.py runserver 0.0.0.0:8000
