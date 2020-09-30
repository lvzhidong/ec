#!/bin/bash

. venv/bin/activate

export PYTHONPATH=${PYTHONPATH}:../

while [[ 0 ]];
do
	python manage.py runserver $*
	sleep 1
done
