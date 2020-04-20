# Py-Packager

Tool is to create egg for python or zip file for pyspark of all the dependencies 
for your project.

## Requirements
We require following tools to run the project:
* Python
* Make

## PreRequisite
Clone the repository

```shell script
git clone git@github.com:bhavintandel/py-packager.git
cd py-packager
```

## Update requirements.txt
Add your required package under requirements.txt. For ex.,

```text
Geocoder
xlrd
```

## Update project details
Update the **version** and *project name* under `setup.py`. For ex.,

```python
VERSION = "0.1.0"
PACKAGE_NAME = "dependencies"
```

This will be used to generate your final files.

## Generate the package

### To build python egg file

```shell script
make bdist_egg
```

### To build pyspark zip file

```shell script
make build_zip
```

### To build all

```shell script
make build
```

## Output files
The above commands will generate your package files under **dist** folder.

