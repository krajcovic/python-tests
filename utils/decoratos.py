#!/usr/bin/python3
# -*- coding: utf-8 -*-

a_string = "This is a global variable"


def dekorator_debug(fce):
    def xprint(*args, **kwargs):
        try:
            if (debug == True):
                fce(*args, **kwargs)
        except NameError:  # debug neni definovan
            pass

    return xprint


@dekorator_debug  # debuginfo = dekorator_debug(debuginfo)
def debuginfo(text):
    print('info: ' + text)


def outer(some_func):
    def inner():
        print("before some_func")
        ret = some_func()
        return ret + 1

    return inner

def foo():
    return 1


class Test:
    def instance_method(self):
        print(self)

    @classmethod
    def class_method(cls):
        print(cls)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    debuginfo('normal')

    print = dekorator_debug(print)

    print('dekorator false')
    debug = True
    debuginfo('Ahoj normal')
    print('dekorator true')

    a = Test()
    print(a.instance_method())
    print(a.class_method())
