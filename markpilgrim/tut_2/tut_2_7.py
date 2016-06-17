#!/usr/bin/env python3

a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
print(a_dict)
print(a_dict['server'])

a_dict['database'] = 'blog'
print(a_dict)
a_dict['user'] = 'mark'
print(a_dict)
a_dict['User'] = 'mark'
print(a_dict)

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

print(len(SUFFIXES))
print(1000 in SUFFIXES)
print(SUFFIXES[1000])
