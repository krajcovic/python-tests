#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import pickle
import pickletools

shell = 1


def protocol_version(file_object):
    """
    Print protocol version
    :param file_object:
    :return:
    """
    maxproto = -1
    for opcode, arg, pos in pickletools.genops(file_object):
        maxproto = max(maxproto, opcode.proto)
    return maxproto


entry = {'title': 'Dive into history, 2009 edition',
         'article_link': 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition',
         'comments_link': None,
         'internal_id': b'\xDE\xD5\xB4\xF8',
         'tags': ('diveintopython', 'docbook', 'html'),
         'published': True,
         'published_date': time.strptime('Fri Mar 27 22:20:42 2009')}
print(entry['published_date'])

with open('entry.pickle', 'wb') as f:
    pickle.dump(entry, f)

b = pickle.dumps(entry)
print(type(b))
print(pickle.loads(b) == entry)

with open('entry.pickle', 'rb') as f:
    print(protocol_version(f))
    # pickletools.dis(f)
