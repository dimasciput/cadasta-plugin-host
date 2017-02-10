SHELL := /bin/bash

run:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Run django app"
	@echo "------------------------------------------------------------------"
	@venv/bin/python manage.py runserver 64455
