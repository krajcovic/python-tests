#!/usr/bin/env python3

a_set = {1}
print(a_set, type(a_set))

a_set = {1, 2}
print(a_set, type(a_set))

a_list = ['a', 'b', 'mpilgrim', True, False, 42]
a_set = set(a_list)
print(a_set, type(a_set))
print(a_list, type(a_list))

a_set = {1, 2}
a_set.add(5)
print(a_set, type(a_set))

a_set.add(1)
print(a_set, type(a_set))

a_set.update({7, 8, 9})
print(a_set, type(a_set))