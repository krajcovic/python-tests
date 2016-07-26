#!/usr/bin/python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import doctest

    doctest.testmod()

    counter = 0
    for i in range(1, 100000001):

        if not i % 100000:
            print('\rTested number: {}'.format(i), end='')

        if not i % 21:
            continue
        if not i % 30:
            continue
        if not i % 105:
            continue

        if (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
            counter += 1

    print('')
    print('Result = ', counter)
