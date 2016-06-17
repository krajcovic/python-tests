#!/usr/bin/env python3

a_string = 'My alphabet starts where your alphabet ends.'
print(a_string[3:11])

by = b'abcd\x65'
by += b'\xff'
print(by, len(by), type(by))
# by[0] = 102

