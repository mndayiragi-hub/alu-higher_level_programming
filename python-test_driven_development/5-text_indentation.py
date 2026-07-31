#!/usr/bin/python3
"""Module that prints text with 2 new lines after ., ? and :"""


def text_indentation(text):
    """Print text with 2 new lines after each ., ? and :

    Args:
        text: the text to print

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    result = ""
    i = 0
    for char in text:
        if char == " " and (len(result) == 0 or result[-1] == "\n"):
            continue
        result += char
        if char in ".?:":
            result += "\n\n"
            i += 1
    print(result.strip())
