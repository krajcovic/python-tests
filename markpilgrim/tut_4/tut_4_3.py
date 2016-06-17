#!/usr/bin/env python3
import sys

s = '深入 Python'
print(s, ": length",len(s))

username = 'mark'
password = 'papayaWhip'
print("{0}'s password is {1}".format(username, password))

print("Help: {0.modules[stat].__doc__}".format(sys))

s = '''Finished files are the re-
sult of years of scientif-
ic study combined with the
experience of years.'''
print(s)
print(s.splitlines())
print(s.lower())
print(s.lower().count('f'))


query = 'user=pilgrim&database=master&password=PapayaWhip'
a_list = query.split('&')
print (a_list)
a_list_of_lists = [v.split('=', 1) for v in a_list if '=' in v]
print(a_list_of_lists)
a_dict = dict(a_list_of_lists)
print(a_dict)