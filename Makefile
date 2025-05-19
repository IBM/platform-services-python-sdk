PYTHON=python
LINT=black
POETRY=poetry
LINT_DIRS=ibm_platform_services test/unit test/integration examples

all: upgrade-pip deps test-unit lint

ci: all

publish-release: build-dist publish-dist

upgrade-pip:
	${PYTHON} -m pip install --upgrade pip

deps:
	${POETRY} install

detect-secrets:
	detect-secrets scan --update .secrets.baseline
	detect-secrets audit .secrets.baseline

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
	${POETRY} build --clean

# This target requires the POETRY_PYPI_TOKEN_PYPI env variable to be set to the user's pypi.org API token.
publish-dist:
	${POETRY} publish --dry-run
