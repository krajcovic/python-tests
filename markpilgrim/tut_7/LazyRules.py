#!/usr/bin/python3
# -*- coding: utf-8 -*-

from markpilgrim.tut_6.tut_6_2 import build_match_and_apply_functions

class LazyRules:
    rules_filename = 'plural6-rules.txt'

    def __int__(self):
        self.patter_file = open(self.rules_filename, encoding='utf-8')
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.patter_file.closed:
            raise StopIteration

        line = self.patter_file.readline()
        if not line:
            self.patter_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = build_match_and_apply_functions(pattern, search, replace)
        self.cache.append(funcs)
        return funcs


rules = LazyRules()
