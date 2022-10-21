
# Makefile
SHELL = /bin/bash

.PHONY: help
help:
	@echo "Commands:"
	@echo "venv    : creates a virtual environment."
	@echo "style   : executes style formatting."
	@echo "clean   : cleans all unnecessary files."
	@echo "test    : execute tests."
	@echo "build   : build package."
	@echo "publish : publish package."

# Styling
.PHONY: style
style:
	black .
	# flake8
	python -m isort .

# Environment
.ONESHELL:
venv:
	python -m venv venv
	source venv/bin/activate && \
	python -m pip install --upgrade pip setuptools wheel 

# Cleaning
.PHONY: clean
clean: style
	find . -type f -name "*.DS_Store" -ls -delete
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	find . | grep -E ".trash" | xargs rm -rf
	rm -rf .coverage

# Test
.ONESHELL:
test:
	pytest tests

# Build
.ONESHELL:
build:
	rm -rf dist *.egg-info
	python setup.py sdist bdist_wheel

# Publish
.ONESHELL:
publish:
	twine upload dist/*