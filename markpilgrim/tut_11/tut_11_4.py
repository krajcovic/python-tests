#!/usr/bin/python3
# -*- coding: utf-8 -*-

import io

with open('beauregard.jpg', mode='rb') as an_image:
    print(an_image.mode)
    print(an_image.name)

a_string = 'PapayaWhip is the new black.'
a_file = io.StringIO(a_string)
a_file.read()
a_file.read()
a_file.seek(0)
a_file.read(10)
a_file.tell()
a_file.seek(18)
print(a_file.read())