#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

o = np.ones([4, 4], dtype=int)
o[2, 3] = 2
o[3, 1] = 6
print(o)

o = np.zeros([6, 6], dtype=float)
o[2, 3] = 2
o[3, 1] = 6
print(o)

print(np.arange(6))
print(np.arange(0, 51, 10)[:, np.newaxis])

print(np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis])



if __name__ == '__main__':
    import doctest

    doctest.testmod()
