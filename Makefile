.PHONY: help check-stage pipme setup update require lint test

help:
	@echo "check-stage - check staged changes for lint errors"
	@echo "pipme - install requirements.txt"
	@echo "setup - setup database"
	@echo "update - update ScraperWiki code"
	@echo "require - create requirements.txt"
	@echo "lint - check style with flake8"
	@echo "test - run nose and script tests"

check-stage:
	bin/check-stage

pipme:
	sudo pip install -r requirements.txt

setup:
	bin/setup

update:
	bin/swupdate

require:
	pip freeze -l | grep -vxFf dev-requirements.txt > requirements.txt

lint:
	flake8 app tests

test:
	nosetests -xv
