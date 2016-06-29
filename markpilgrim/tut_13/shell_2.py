#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pickle

with open('entry.pickle', 'rb') as f:
    entry = pickle.load(f)

print(entry, sep='\n')

