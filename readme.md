## python_project
A template setup for a python project.

It contains the following:
* TravisCI for continuous integration
* unittest for testing the project libraries
* Documentation on readthedocs.org built using Sphinx, Doxygen and breathe.
* Packaging the library for distribution on PyPi

The template documentation for this project is on [readthedocs](https://cpp-project-setup.readthedocs.io/en/latest/).

### Usage
- Delete *lib.py files in python_project
- Delete *.py files in tests dir and add your own tests there.
- Replace python_project with your project name

#### Build Status
<img src="https://travis-ci.com/wasimusu/python_project.svg?branch=master" width="100">
<img src="https://readthedocs.org/projects/graphs/badge/?version=latest">


### Platform
* Linux (Xenial/Ubuntu 18.04)


### Generating Documentation
To generate documentation on readthedocs.org, do the following:
- On readthedocs.org, select your project for generating documentation and build.

To generate documentation locally each time you change the documentation:
```
cd docs
make clean
doxygen Doxyfile
make html
```
Open the docs/build/html/index.html in your browser to view the documentation on localhost.

### Setting up a distribution on PyPi
Please follow the following resource for setting up package distribution.