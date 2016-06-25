#!/usr/bin/python3
# -*- coding: utf-8 -*-

import locale

print('Preffered coding: {}'.format(locale.getpreferredencoding()))

with open('chinese.txt', mode='r', encoding='utf-8') as a_file:
    # a_file = open('chinese.txt', mode='r')
    print(a_file.name, a_file.encoding, a_file.mode)
    a_string = a_file.read()
    print(a_string)
    print(a_file.read())

    a_file.seek(0)
    print(a_file.readline(), end='')
    print(a_file.readline(), end='')

# a_file.close()
# try:
#     a_file.read()
# except ValueError:
#     pass
#
# if not a_file.closed:
#     a_file.close()
