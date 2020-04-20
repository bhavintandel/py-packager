# Get the version of from setup.py
VERSION=$(shell grep "VERSION = [0-9.]*" setup.py | cut -d\" -f2)
PROJECT_NAME=$(shell grep "PACKAGE_NAME = *" setup.py | cut -d\" -f2)

clean:
	rm -f -r libs/
	rm -f -r build/
	rm -f -r dist/
	rm -f -r *.egg-info

build: clean build_zip bdist_egg

bdist_egg:
	python setup.py bdist_egg

sdist_zip:
	python setup.py sdist --format=zip

build_zip:
	mkdir -p libs dist
	pip install -r requirements.txt -t libs
	(cd libs; zip -r ../dist/${PROJECT_NAME}-${VERSION}.zip *)
	rm -rf libs/



