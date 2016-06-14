#!/usr/bin/env python3

import sys

print(type(None))

print(bin(25))
print((25).bit_length())
print(hex(25))

print((1023).to_bytes(4, byteorder=sys.byteorder))
print((1023).to_bytes(4, byteorder=sys.byteorder))