# !/bin/bash

# Django project directory
DJANGODIR=/home/to-website
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

# how many worker processes should Gunicorn spawn
NUM_WORKERS=3

# if we communicte using the unix socket
SOCKFILE=$DJANGODIR/gunicorn.sock
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start nginx server
rm -rf /etc/nginx/sites-enabled/default
cp $DJANGODIR/config/nginx.conf /etc/nginx/conf.d
service nginx start

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--bind=unix:$SOCKFILE \
--timeout 120 \
--log-level=debug \
--access-logfile=/home/to-website/logs/gunicorn_access.log \
--error-logfile=/home/to-website/logs/gunicorn_error.log
