#!/usr/bin/env python3

import logging

a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
print(a_list)
for item in a_list:
    print(item, type(item))

n = 2
print(a_list[-n] == a_list[len(a_list) - n])

print(a_list[1:3])
print(a_list[1:-1])
print(a_list[0:3])
print(a_list[:3])

a_list = ['a']
a_list = a_list + [2.0, 3]
print(a_list)
a_list.append(True)
print(a_list)

a_list = ['a', 'b', 'c']
a_list.extend(['d', 'e', 'f'])
print(a_list)
print(len(a_list))

a_list.append(['g', 'h', 'i'])
print(a_list)
print(len(a_list))

a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
print(a_list.count('new'))

print('new'.strip() in a_list)

print(a_list.index('new'))

try:
    print(a_list.index('x'))
except ValueError as e:
    print(e)
    #logging.exception(e)


print(a_list)
del a_list[1]
for i in range(a_list.count('new')):
    a_list.remove('new')

print(a_list)

