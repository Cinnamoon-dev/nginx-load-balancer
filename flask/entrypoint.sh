#!/usr/bin/env bash

python3 app.py db init &&
python3 app.py db migrate &&
python3 app.py db upgrade &&
python3 app.py runserver
