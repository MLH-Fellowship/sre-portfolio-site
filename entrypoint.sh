#!/bin/sh
flask db migrate
flask db upgrade
gunicorn wsgi:app -w 1 -b 0.0.0.0:80 --capture-output --log-level debug
