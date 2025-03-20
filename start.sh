#!/bin/bash
. .venv/bin/activate
export $(grep -v '^#' .env | xargs)
python manage.py runserver 0.0.0.0:8002
