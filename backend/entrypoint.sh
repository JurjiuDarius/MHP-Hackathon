#!/bin/sh
python manage.py db upgrade
flask run --host=0.0.0.0


