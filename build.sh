#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python mana.py collectstatic --noinput
python manage.py migrate
