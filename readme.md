## python_project
A template setup for a python project.

It contains the following:
* Setting up a python package
* unittest for testing the project libraries
* TravisCI for continuous integration
* Documentation on readthedocs.org built using Sphinx, Doxygen and breathe.
* Packaging the library for distribution on PyPi

The template documentation for this project is on [readthedocs](https://python-project-setup.readthedocs.io/en/latest/).

### Usage
- Clone this project:
```
git clone https://github.com/wasimusu/python_project.git
```
- Delete *lib.py files in python_project. This is where you will write your libraries
- Delete *.py files in tests dir. Add your own tests here.
- Replace python_project with your project name

#### Build Status
<img src="https://travis-ci.com/wasimusu/python_project.svg?branch=master" width="100">
<img src="https://readthedocs.org/projects/python-project-setup/badge/?version=latest">

### Platform
* Linux (Xenial/Ubuntu 18.04)
* Python 3.5, 3.7

### Generating Documentation
Generating documentation locally:
```
doxygen -g Doxyfile
```
Change the PROJECT_NAME in Doxyfile.
```
doxygen Doxyfile
```
Now let's do the sphinx part
```
sphinx-quickstart
```

These are the prompts you get. We're going for a simple documentation setup here.

```
> Separate source and build directories (y/n) [n]: n
> Project name: python_project
> Author name(s): Wasim Akram Khan
> Project release []: 0.0.1
> Project language [en]:
```

Sphinx should have generated an index.rst file in docs directory. Go make some changes to the conf.py and index.rst as
shown in files docs/conf.py and docs/index.rst.

```
make html
```
We have now setup the documentation. Open the docs/build/html/index.html in your browser to view the documentation on localhost.

#### If you're not seeing your source files indexed/documented then it's probably path error. Make sure your source files are discoverable.
You can do this by testing different values for sys.path.insert()


To re-generate documentation locally each time you change the documentation:
```
cd docs
make clean
doxygen Doxyfile
make html
```
Open the docs/build/html/index.html in your browser to view the documentation on localhost.

#### Readthedocs
To generate documentation on readthedocs.org, do the following:
- Make an account on readthedocs.org if you have not already.
- On readthedocs.org, select your project for generating documentation and build.


### Run all tests
Discovers all the files named test*.py and runs all the unittest.
```
python -m unittest discover tests
```

### TravisCI (Continuous Integration)
Basically all you need is an account on travis-ci.com and link your github account. Whenever you push a project containing
.travis.yml file to github the TravisCI is triggered. It builds the projects, runs tests and/or benchmarks as defined in
the .travis.yml file.

Defining .travis.yml is simple. You only need to define what versions of Python you want to test and what platforms. You
also need to provide instructions on how to run your code just like you'd explain on your github readme to potential users.

### Packaging the python_project for distribution on pypi.org
MANIFEST.in and setup.py are files that define the packaging. If you've followed the structure of this project, you're setup
for distribution. Please refer to this to see the instructions to build your package and upload it to pypi.org.