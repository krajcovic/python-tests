#!/usr/bin/env python3

import os
import glob

os.chdir('../tut_2')

metada = [(f, os.stat(f)) for f in glob.glob('*.py')]
print(metada)

metata_dict = {f:os.stat(f) for f in glob.glob('*.py') if os.stat(f).st_size > 200}
print(metata_dict)
print("\n".join(list(metata_dict.keys())))

print("tut_2_5.py size =", metata_dict['tut_2_5.py'].st_size)

a_dict = {'a': 1, 'b': 2, 'c':3}
print({value:key for key, value in a_dict.items()})

