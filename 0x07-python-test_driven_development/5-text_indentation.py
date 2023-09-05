#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after a set of characters.
"""


def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for punctuation in ".:?":
        text = (punctuation + "\n\n").join(
            [line.strip(" ") for line in text.split(punctuation)])

    print("{}".format(text), end="")
