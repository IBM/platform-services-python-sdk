# This makefile is used to make it easier to get the project set up
# to be ready for development work in the local sandbox.
# example: "make setup"

setup: deps dev_deps install_project

all: setup test-unit lint

deps:
	python -m pip install -r requirements.txt

dev_deps:
	python -m pip install -r requirements-dev.txt

install_project:
	python -m pip install -e .

test: test-unit test-int

test-unit:
	python -m pytest test/unit

test-int:
	python -m pytest test/integration

lint:
	./pylint.sh
