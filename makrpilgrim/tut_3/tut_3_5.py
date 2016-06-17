#!/usr/bin/env python3

a_set = set(range(10))
print(sorted(a_set))
print(sorted({x ** 2 for x in a_set}))
print(sorted({x for x in a_set if x % 2 == 0}))
print(([2**x for x in range(10)]))