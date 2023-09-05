# This makefile is used to make it easier to get the project set up
# to be ready for development work in the local sandbox.
# example: "make setup"

PYTHON=python
LINT_DIRS=ibm_platform_services test examples

setup: deps dev_deps install_project

all: upgrade_pip setup test-unit lint

ci: setup test-unit lint

upgrade_pip:
	${PYTHON} -m pip install --upgrade pip

deps:
	${PYTHON} -m pip install -r requirements.txt

dev_deps:
	${PYTHON} -m pip install -r requirements-dev.txt

install_project:
	${PYTHON} -m pip install -e .

test: test-unit test-int

test-unit:
	${PYTHON} -m pytest --cov=ibm_platform_services test/unit

test-int:
	${PYTHON} -m pytest test/integration

test-examples:
	${PYTHON} -m pytest examples

lint:
	${PYTHON} -m pylint ${LINT_DIRS}
	black --check ${LINT_DIRS}

lint-fix:
	black ${LINT_DIRS}
