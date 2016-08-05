#!/usr/bin/python3
# -*- coding: utf-8 -*-

# from numpy import *
import numpy as np


def example1():
    a = np.arange(15).reshape(3, 5)
    print(a)
    print(np.shape(a))
    print(a.ndim)
    print(a.dtype.name)
    print(a.itemsize)
    print(a.size)
    print(type(a))
    b = np.array([6, 7, 8])
    print(b)
    print(type(b))


def array_creation():
    a = np.array(range(2, 5))
    print(a)
    print(a.dtype)
    b = np.array([1.2, 3.5, 5.1])
    print(b.dtype)

    a = np.array([1, 3, 5])
    print(a)

    b = np.array([(1.5, 2, 3), (4, 5, 6)])
    print(b)

    c = np.array([[1, 2], [3, 4]], dtype=complex)
    print(c)


def zeros_creation():
    print(np.zeros([3, 4]))
    print(np.ones([2, 3, 4], dtype=int))
    print(np.empty([2, 3]))

    print(np.arange(10, 30, 5))
    print(np.arange(0, 2, 0.3))

    print(np.linspace(0, 2, 9))

    x = np.linspace(0, 2 * np.pi, 100)
    print(np.sin(x))


def printing_arrays():
    a = np.arange(6)
    print(a)
    b = np.arange(12).reshape(4, 3)
    print(b)
    c = np.arange(24).reshape(2, 3, 4)
    print(c)

    # print(np.arange(1000))
    print(np.arange(16 * 16).reshape(16, 16))


def shape_manipulation():
    a = np.floor(10 * np.random.random((3, 4)))
    # a = (10 * np.random.random((3, 4)))
    print(a)
    print(a.ravel())
    a.shape = (6, 2)
    print(a.transpose())
    a.resize((6, 2))
    print(a)


def vector_stacking():
    x = np.arange(0, 10, 2)  # x=([0,2,4,6,8])
    print(x)
    y = np.arange(5)  # y=([0,1,2,3,4])
    print(y)
    m = np.vstack([x, y])  # m=([[0,2,4,6,8],
    print(m)
    #     [0,1,2,3,4]])
    xy = np.hstack([x, y])  # xy =([0,2,4,6,8,0,1,2,3,4])
    print(xy)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    # example1()
    # array_creation()
    # zeros_creation()
    # printing_arrays()
    # shape_manipulation()
    vector_stacking()
