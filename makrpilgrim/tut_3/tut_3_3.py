#!/usr/bin/env python3

import os
import glob

a_list = [1, 9, 8, 4]
a_list2 = [elem * 2 for elem in a_list]
print(*a_list, sep='\t')
print(*a_list2, sep='\t')

print(glob.glob('*.py'))
os.chdir('../tut_2')
[print((f, os.path.realpath(f))) for f in glob.glob('*.py') if os.stat(f).st_size > 400]
print(glob.iglob('*'))
