#!/usr/bin/env bash

python3 flask_app.py db init
python3 flask_app.py db migrate
python3 flask_app.py db upgrade
python3 flask_app.py runserver