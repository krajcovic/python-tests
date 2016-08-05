#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

np.random.seed(3)
a = np.random.random_integers(0, 20, 15)
[print(i, i % 3 == 0, sep='\t') for i in a]
mask = (a % 3 == 0)
extract_from_a = a[mask]
print(extract_from_a)

a[a % 3 == 0] = -1
print(a)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

