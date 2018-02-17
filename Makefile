RUNTEST=python3
ALLMODULES =$(wildcard *test.py)

all:
	for tt in $(ALLMODULES); do echo $$tt; $(RUNTEST) $$tt; done

