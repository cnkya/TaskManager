#!/usr/bin/env sh

export Flask_APP=app/routes.py
export FLASK_ENV=development

flask run
