#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import itertools
import sys


def test_solve():
    assert solve("HAWAII + IDAHO + IOWA + OHIO == STATES") == "510199 + 98153 + 9301 + 3593 == 621246"
    # assert solve("I + LOVE + YOU == DORA") == "1 + 2457 + 948 == 3406"
    assert solve("SEND + MORE == MONEY") == "9567 + 1085 == 10652"


def solve(p):
    """
    Solve alphametics.
    :param p:
    :return:

    >>> solve("HAWAII + IDAHO + IOWA + OHIO == STATES")
    '510199 + 98153 + 9301 + 3593 == 621246'

    """
    words = re.findall('[A-Z]+', p.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = p.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation


def test_find_characters():
    assert re.findall('[0-9]+', '16 2-by-4s in rows of 8') == ['16', '2', '4', '8']
    assert re.findall('[A-Z]+', 'SEND + MORE == MONEY') == ['SEND', 'MORE', 'MONEY']


def findUniqOrder():
    a_list = ['The', 'sixth', 'sick', "sheik's", 'sixth', "sheep's", 'sick']
    print(set(a_list))
    a_string = 'EAST IS EAST'
    print(set(a_string))
    words = ['SEND', 'MORE', 'MONEY']
    print(''.join(words))
    print(set(''.join(words)))


def genExpression():
    unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
    print(tuple(ord(c) for c in unique_characters))
    gen = (ord(c) for c in unique_characters)  # generatovy vyraz
    gen = ord_map(unique_characters)  # generatova funkce - obe delaji to same
    print(gen)
    for i in range(len(unique_characters)):
        value = next(gen)
        print(chr(value), value)


def ord_map(a_string):
    for c in a_string:
        yield ord(c)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    for puzzle in sys.argv[1:]:
        print(puzzle)
    solution = solve(puzzle)
    if solution:
        print(solution)
