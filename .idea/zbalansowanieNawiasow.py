#!/usrs/bin/env python3

import re

NAWIASY = ['(', ')', '{', '}', '[', ']', '<', '>']
REGEX = '[' + '\\'.join(NAWIASY) + ']'

def zbalansowanie_nawiasow(dane):
    """
    >>> dane = "() [] () ([]()[])"
    >>> zbalansowanie_nawiasow(dane)
    True
    >>> dane = "( (] ([)]"
    >>> zbalansowanie_nawiasow(dane)
    False
    """

    same_nawiasy = re.findall(REGEX, dane)

    if not len(same_nawiasy) % 2:
        return False

    pozycja = 0
    for znak in dane:
        pozycja += 1
