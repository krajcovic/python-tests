#!/usr/bin/python3
# -*- coding: utf-8 -*-

line_number = 0
with open('favorite-people.txt', encoding='utf-8') as a_file:
    for a_line in a_file:
        line_number += 1
        test = '{' + ':>{0}'.format(line_number) + '} + {}'
        print(test.format(line_number, a_line.rstrip()))
        # print('{:>4} {}'.format(line_number, a_line.rstrip()))


with open('test.log', mode='w', encoding='utf-8') as a_file:
    a_file.write('test succeeded')


with open('test.log', encoding='utf-8') as a_file:
    print(a_file.read())


with open('test.log', mode='a', encoding='utf-8') as a_file:
    a_file.write('and again')

with open('test.log', encoding='utf-8') as a_file:
    print(a_file.read())