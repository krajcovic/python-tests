#!/usr/bin/env python3

a_string = 'My alphabet starts where your alphabet ends.'
print(a_string[3:11])

by = b'abcd\x65'
# by += b'\xff'
print(by, len(by), type(by))
# by[0] = 102

barr = bytearray(by)
print(barr, len(barr), type(barr))
barr[0] = 102
print(barr, len(barr), type(barr))
de = by.decode('ascii')
print(de, len(de), type(de))

a_string = '深入 Python'
print(len(a_string))
by = a_string.encode('utf-8')
print(by, type(by))

