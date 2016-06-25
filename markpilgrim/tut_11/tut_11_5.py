#!/usr/bin/python3
# -*- coding: utf-8 -*-

import gzip
import sys

with gzip.open('out.log.gz', mode='wb') as z_file:
    z_file.write('A nine mile walls is no joke, especially in the rain.'.encode('utf-8'))

for i in range(3):
    sys.stderr.write('new black')


class RedirectStdoutTo:
    def __init__(self, out_new):
        self.out_new = out_new

    def __enter__(self):
        self.out_old = sys.stdout
        sys.stdout = self.out_new

    def __exit__(self, *args):
        sys.stdout = self.out_old


print('A')
with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):
    print('B')
print('C')
