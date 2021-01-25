all:
	@echo "no default make rule defined"

help:
	cat Makefile

test:
	pytest -vs tests

requirements:
	python3 -m pip install --upgrade -r requirements.txt

requirements-dev:
	python3 -m pip install --upgrade -r requirements-dev.txt

build: clean
	python3 setup.py build install

clean:
	rm -fr build dist __pycache__ *.egg-info/
