Python Project
**************
A template setup for a python project.

Features
========
It contains the following:
   * TravisCI for continuous integration
   * unittest for testing the project libraries
   * Documentation on readthedocs.org built using Sphinx, Doxygen and breathe.
   * Packaging the library for distribution on PyPi


Code snippets in rst file
=========================
sample.py

.. code-block:: python
   :name: sample.py

    from python_project import mathlib

    sum = mathlib.add(1, 1)
    print(f"Sum : {sum}")

APIs
====
.. toctree::
   :maxdepth: 2
   :caption: Contents:

This package provides two different types of APIs.

Math Lib
========
.. automodule:: python_project.mathlib
   :members:

String Lib
==========
.. automodule:: python_project.strlib
   :members:
