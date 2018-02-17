RUN_PY_TEST=python3
RUN_PY_LINT=pylint
ALL_PY_MODULES:=$(wildcard *.py)
ALL_PY_TESTS:=$(wildcard *_test.py)
PY_LINT_TARGETS:=$(addsuffix .lint_out , $(ALL_PY_MODULES))
PY_TEST_TARGETS:=$(addsuffix .test_out , $(ALL_PY_TESTS))

all: $(PY_LINT_TARGETS) $(PY_TEST_TARGETS)

clean:
	rm -f $(PY_LINT_TARGETS) $(PY_TEST_TARGETS)

print-%  : ; @echo $* = $($*)

%.py.lint_out : %.py
	$(RUN_PY_LINT) $<
	touch $@

%.py.test_out : %.py $(ALL_PY_MODULES)
	$(RUN_PY_TEST) $<
	touch $@
