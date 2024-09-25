#!/usr/bin/env bash
set -e

python manage.py migrate

gunicorn -cpython:gunicorn_config -b 0.0.0.0:${DJANGO_BIND_PORT:-$PORT} book.wsgi
