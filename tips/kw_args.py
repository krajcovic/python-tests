#!/usr/bin/python3
# -*- coding: utf-8 -*-


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    test_var_args('yasoob', 'python', 'eggs', 'test')
