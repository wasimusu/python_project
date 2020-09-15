"""
Objective: use functions of the package we built
"""

from python_project import mathlib
from python_project import strlib


def nums_and_strings():
    """
    A simple function demonstrating the usage of libraries built in this package
    :return: None
    """
    num_fruits = len(strlib.split("apple mango orange"))
    num_colors = len(strlib.split("red,yellow,orange", ','))
    total = mathlib.add(num_fruits, num_colors)
    print("Total : {}".format(total))


if __name__ == '__main__':
    nums_and_strings()
