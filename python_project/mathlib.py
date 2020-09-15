"""
Implements library for algebraic operations on integers
"""


def add(first_number: int, second_number: int) -> int:
    """
    Adds two integers

    :param first_number, second_number: two numbers to be added

    :return: [int] sum of the two input numbers

    :raise ValueError if the numbers are not integers
    """
    if isinstance(first_number, int) and isinstance(second_number, int):
        return first_number + second_number
    else:
        raise ValueError(
            "Invalid error. Expected (int, int) got ({}, {})".format(type(first_number), type(second_number)))
