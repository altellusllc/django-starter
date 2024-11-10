#!/bin/bash
. .venv/bin/activate
export $(grep -v '^#' .env | xargs)
python manage.py runserver 100.93.58.95:8000
