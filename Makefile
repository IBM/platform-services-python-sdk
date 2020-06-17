# This makefile is used to make it easier to get the project set up
# to be ready for development work in the local sandbox.
# example: "make setup"

setup: deps dev_deps install_project

deps:
	pip install -r requirements.txt

dev_deps:
	pip install -r requirements-dev.txt

install_project:
	pip install -e .
