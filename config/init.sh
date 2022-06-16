# !/bin/bash

# which settings file should Django use
DJANGO_SETTINGS_MODULE=towebsite.settings

# WSGI module name
DJANGO_WSGI_MODULE=towebsite.wsgi
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# # Make migrations
# echo "Make migrations"
# python manage.py makemigrations
# python manage.py makemigrations main

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Name of the application
NAME="to-website"

# Django project directory
DJANGODIR=/home/to-website

# how many worker processes should Gunicorn spawn
NUM_WORKERS=3

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--bind=0.0.0.0:8000 \
--log-level=debug \
--access-logfile=/home/to-website/logs/gunicorn_access.log \
--error-logfile=/home/to-website/logs/gunicorn_error.log
