#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

roman_numeral_map = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1))

roman_numeral_pattern = re.compile('''
    ^                   # začátek řetězce
    M{0,3}              # tisíce - 0 až 3 M
    (CM|CD|D?C{0,3})    # stovky - 900 (CM), 400 (CD), 0-300 (0 až 3 C),
    (XC|XL|L?X{0,3})    # nebo 50-80 (L následované 0 až 3 X)
    (IX|IV|V?I{0,3})    # jednotky - 9 (IX), 4 (IV), 0-3 (0 až 3 I),
    $                   # konec řetězce
    ''', re.VERBOSE)


class OutOfRangeError(ValueError):
    """
    Exception class for invalid values.
    """
    pass


class NotIntegerError(ValueError):
    """
    Exception class for non integers values.
    """
    pass


class InvalidRomanNumeralError(ValueError):
    """
    Exception class for invalid values
    """
    pass


def to_roman(n):
    """
    Convert integer to Roman numeral
    :param n:
    :return:
    """

    if not isinstance(n, int):
        raise NotIntegerError('non-integers can not be converted')

    # if n <= 0 or n > 3999:
    if not (0 < n < 4000):
        raise OutOfRangeError('number out of range (must be over 0 and less than 4000')

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
            # print('subtracting {0} from input, adding {1} to output'.format(integer, numeral))
    return result


def from_roman(s):
    """
    Convert Roman numeral to integer
    :param numeral:
    :return:
    """
    if not roman_numeral_pattern.search(s):
        raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))

    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
            # print('found', numeral, 'of length', len(numeral), ', adding', integer)
    return result
