#!/bin/bash

# Wait for database to be ready
echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Database started"

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Start server
echo "Starting server..."
exec "$@"