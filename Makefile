# This makefile is used to make it easier to get the project set up
# to be ready for development work in the local sandbox.
# example: "make setup"

PYTHON=python
LINT=black
LINT_DIRS=ibm_platform_services test/unit test/integration examples

setup: deps dev-deps install-project

all: upgrade-pip setup test-unit lint

ci: all

publish-release: publish-deps build-dist publish-dist

upgrade-pip:
	${PYTHON} -m pip install --upgrade pip

deps:
	${PYTHON} -m pip install .

dev-deps:
	${PYTHON} -m pip install .[dev]

detect-secrets:
	detect-secrets scan --update .secrets.baseline
	detect-secrets audit .secrets.baseline

publish-deps:
	${PYTHON} -m pip install .[publish]

install-project:
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
	${LINT} --check ${LINT_DIRS}

lint-fix:
	${LINT} ${LINT_DIRS}

build-dist:
	rm -fr dist
	${PYTHON} -m build

# This target requires the TWINE_PASSWORD env variable to be set to the user's pypi.org API token.
publish-dist:
	TWINE_USERNAME=__token__ ${PYTHON} -m twine upload --non-interactive --verbose dist/*
