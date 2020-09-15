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
    return string.split(delimiter)
