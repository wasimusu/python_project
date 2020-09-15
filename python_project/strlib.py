"""
Implements library to manipulate text
"""


def split(string: str, delimiter: str = ' ') -> list:
    """
    Splits string based on input delimiter

    :param string: input string/text to be split based on delimiter
    :param delimiter: input delimiter to split the user text
    :return: [list[str]] list of splitted strings
    """
    if isinstance(string, str) and isinstance(delimiter, str):
        return string.split(delimiter)
    raise ValueError(
        "Expected (string, delimiter) of type (str, str) got ({}, {}). ".format(type(string), type(delimiter)))
