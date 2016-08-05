#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

is_prime = np.ones((100,), dtype=bool)
print(is_prime)
is_prime[:2] = 0
print(is_prime)

N_max = int(np.sqrt(len(is_prime)))
# print(N_max)
for j in range(2, N_max):
    is_prime[2 * j::j] = False
print(is_prime)
print(np.nonzero(is_prime))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
