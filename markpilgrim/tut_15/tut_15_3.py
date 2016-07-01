#!/usr/bin/python3
# -*- coding: utf-8 -*-

import chardet

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(chardet.detect(b'\xffZkouska'))