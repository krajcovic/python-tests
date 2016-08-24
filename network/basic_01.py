#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np


def test_T():
    x = np.array([[1., 2.], [3., 4.]])
    print(x)


X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
# print(X)
y = np.array([[0, 1, 1, 0]]).T
# print(y)
syn0 = 2 * np.random.random((3, 4)) - 1
# print(syn0)
syn1 = 2 * np.random.random((4, 1)) - 1
# print(syn1)

for j in range(60000):
    l1 = 1 / (1 + np.exp(-(np.dot(X, syn0))))
    l2 = 1 / (1 + np.exp(-(np.dot(l1, syn1))))

    l2_delta = (y - l2) * (l2 * (1 - l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1 - l1))  # l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))

    syn1 += l1.T.dot(l2_delta)  # syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)
