# Makefile

SHELL := /bin/bash

.PHONY: default test-full isort clean-pyc clean-full


default: test-full

&venv-activate:
	source venv/bin/activate

run: &venv-activate
	python -m vika

venv:
	python3 -m venv venv

install-deps-prod: requirements.txt
	./venv/bin/pip install -r requirements.txt

install-deps-dev: requirements-dev.txt
	./venv/bin/pip install -r requirements-dev.txt

pytest: clean-pyc
	./venv/bin/python -m py.test

isort:
	./venv/bin/python -m isort vika/

black:
	./venv/bin/python -m black vika/

flake8:
	./venv/bin/python -m flake8 vika/

test-full: isort black flake8 pytest vika/tests

clean-full:
	find ./vika -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +

clean-pyc:
	find ./vika -name '*.pyc' -exec rm -f {} +
	find ./vika -name '*.pyo' -exec rm -f {} +
