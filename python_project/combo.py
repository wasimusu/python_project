from python_project.strlib import split
from python_project.mathlib import add


def split_string_add_nums(expr: str):
    """
    Splits string into numbers by comma
    Converts nums into ints
    Adds them
    :param expr: str
    :return: int
    """
    a, b = split(expr, ",")
    a = int(a)
    b = int(b)
    return add(a, b)


if __name__ == '__main__':
    res = split_string_add_nums("1,2")
    print(res)
