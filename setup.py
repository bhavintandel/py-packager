from setuptools import setup, find_packages

VERSION = "0.1.0"

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r+") as f:
    long_description = f.read()

setup(
    name="dependencies",
    version=VERSION,
    description="Project to package dependencies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["docs", "tests", ".gitignore", "README.md", "Makefile"]),
    include_data_files=True,
    zip_safe=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7'
)
