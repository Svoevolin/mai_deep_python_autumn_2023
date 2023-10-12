PYTHON = python3

.PHONY: run test

venv:
	$(PYTHON) -m venv venv

activate_venv:
	source venv/bin/activate

dependencies:
	pip install -r requirements.txt

test:
	$(PYTHON) -m unittest test.py

clean:
	rm -rf __pycache__
