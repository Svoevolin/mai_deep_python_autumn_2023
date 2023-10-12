VIRTUAL_ENV=env
PYTHON=${VIRTUAL_ENV}/bin/python3

.PHONY: run clean venv test

clean:
	rm -rf $(VIRTUAL_ENV)

venv: $(VIRTUAL_ENV)

$(VIRTUAL_ENV):
	python3 -m pip install --upgrade pip
	python3 -m pip install virtualenv
	virtualenv $(VIRTUAL_ENV)

install: venv requirements.txt
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m unittest test.py

