#!/bin/sh
flask db migrate
flask db upgrade

if [ "$FLASK_ENV" = "development"]
then
    echo "Running Flask Development Server"
    flask run --host=0.0.0.0 --port=80
else
    gunicorn wsgi:app -w 1 -b 0.0.0.0:80 --capture-output --log-level debug
fi
