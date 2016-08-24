#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np


def test_dot(A, B):
    """
    If x and y are vectors, this is a dot product. If both are matrices, it's a matrix-matrix multiplication. If only one is a matrix, then it's vector matrix multiplication
    :return:
    >>> test_dot(np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1, 2], [3, 4], [5, 6]]))
    array([[22, 28],
           [49, 64]])
    """

    return np.dot(A, B)


def nonlin(x, deriv=False):
    """
    sigmoid function
    :param x:
    :param deriv:
    :return:
    """
    if deriv == True:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input dataset matrix where each row is a training example
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

# output dataset matrix where earch row is a training example
y = np.array([[0, 1, 1, 0]]).T

# seed random numbers to make calculation deterministic (just for good practice)
np.random.seed(1)

# initialize weight randomly with mean 0
syn0 = 2 * np.random.random((3, 1)) - 1  # first layer of weights, Synapse 0, connection l0 to l1

for iter in range(10000):
    # forward propagation
    l0 = X  # first layer of the network, specified by the input data
    l1 = nonlin(np.dot(l0, syn0))  # Second layer of the network, otherwise known a s the hidden layer
    # print("Output By Training:")
    # print(l1)

    # how much did we miss
    l1_error = y - l1

    # multiply how much we missed by the slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1, True)

    # update weights
    syn0 += np.dot(l0.T, l1_delta)

print("Output After Training:")
print(l1)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
