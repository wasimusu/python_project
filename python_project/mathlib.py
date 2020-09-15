"""
Implements library for algebraic operations on integers
"""


def add(first_number: int, second_number: int) -> int:
    """
    Adds two integers

    :param first_number, second_number: two numbers to be added

    :return: [int] sum of the two input numbers
    """
    try:
        return first_number + second_number
    except:
        raise ValueError(f"Invalid error. Expected (int, int) got ({type(first_number)},{type(second_number)})")
