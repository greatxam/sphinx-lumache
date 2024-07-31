import string
from random import random


def get_random_password(length):
    """
    Generates a random password of given length.
    :param length:
    :return:
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    return ["shells", "gorgonzola", "parsley"]


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass
