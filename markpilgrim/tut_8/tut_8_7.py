#!/usr/bin/python3
# -*- coding: utf-8 -*-

import itertools

names = list(open('favorite-people.txt', encoding='utf-8'))
print(names)
names = [name.strip() for name in names]
print(names)
names = sorted(names)
print(names)
names = sorted(names, key=len)
print(names)

# names = sorted(names, key=hash)
# print(names)

groups = itertools.groupby(names, len)
print(groups)
print(list(groups))
groups = itertools.groupby(names, len)
for name_length, name_iter in groups:
    print('Names with {0:d} letters:'.format(name_length))
    for name in name_iter:
        print(name)

print(list(range(0, 3)))
print(list(range(10, 13)))
print(list(itertools.chain(range(0, 3), range(10, 13))))
print(list(zip(range(0, 3), range(10, 13))))
print(list(zip(range(0, 3), range(10, 15))))
print(list(itertools.zip_longest(range(0, 3), range(10, 15))))

characters = ('S', 'M', 'E', 'D', 'O', 'N', 'R', 'Y')
guess = ('1', '2', '0', '3', '4', '5', '6', '7')
print(tuple(zip(characters, guess)))
print(dict(zip(characters, guess)))

translation_table = {ord('A'): ord('O')}
print(translation_table)
print('MARK'.translate(translation_table))

characters = tuple(ord(c) for c in 'SMEDONRY')
print(characters)
guess = tuple(ord(c) for c in '91570682')
print(guess)
translation_table = dict(zip(characters, guess))
print(translation_table)
print('SEND + MORE == MONEY'.translate(translation_table))
print(eval('1+1==2'))
print(eval('1+1==3'))
print(eval('SEND + MORE == MONEY'.translate(translation_table)))

print(eval('"A" + "B"'))
print(eval('"MARK".translate({65: 79})'))
print(eval('"AAAAA".count("A")'))


