RUN_PY_TEST=python3
RUN_PY_LINT=pylint
ALL_PY_MODULES =$(wildcard *.py)
ALL_PY_TESTS =$(wildcard *test.py)

all: lint tests

lint:
	for ff in $(ALL_PY_MODULES); do echo $$ff; $(RUN_PY_LINT) $$ff; done

tests:
	for tt in $(ALLMODULES); do echo $$tt; $(RUN_PY_TEST) $$tt; done

