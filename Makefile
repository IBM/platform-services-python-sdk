# This makefile is used to make it easier to get the project set up
# to be ready for development work in the local sandbox.
# example: "make setup"

setup: deps dev_deps install_project

all: upgrade_pip setup test-unit lint

ci: setup test-unit lint publish_coverage

upgrade_pip:
	python -m pip install --upgrade pip

deps:
	python -m pip install -r requirements.txt

dev_deps:
	python -m pip install -r requirements-dev.txt

install_project:
	python -m pip install -e .

test: test-unit test-int

test-unit:
	python -m pytest --cov=ibm_platform_services test/unit

publish_coverage:
	codecov

test-int:
	python -m pytest test/integration

test-examples:
	python -m pytest examples

lint:
	./pylint.sh
