.PHONY: default
default: test

envname=env

PYTHON?=python3
VIRTUALENV?=virtualenv3
PIP?=pip3

.PHONY: deps
deps: env/bin/activate

requirements.txt:
	pip freeze > requirements.txt

env/bin/activate: requirements.txt dev-requirements.txt
	virtualenv $(envname)
	@echo "Your virtualenv is setup at $(envname)"
	env/bin/pip install -r dev-requirements.txt
	@echo "and your pip requirements have been installed"
	@echo "run this command to add this virtualenv to your \$$PATH:"
	@echo "source env/bin/activate"
	@echo
	@echo "Later, when you are done with this project you can run this:"
	@echo "deactivate"

.PHONY: test
test:
	tox

.PHONY: clean
clean:
	rm -rf *.egg-info
