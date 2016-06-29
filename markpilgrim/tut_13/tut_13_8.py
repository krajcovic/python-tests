#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import time

basic_entry = {
    "id": 256,
    "title": "Dive into history, 2009 edition",
    "tags": ('diveintopython', 'docbook', 'html'),
    "published": True,
    "comments_link": None,
}

basic_entry_bytes = {
    "id": 256,
    'internal_id': b'\xDE\xD5\xB4\xF8',
    "title": "Dive into history, 2009 edition",
    "tags": ('diveintopython', 'docbook', 'html'),
    # "published_date": time.struct_time(m_year=2009, tm_mon=3, tm_mday=27, tm_hour=22,
    #                                   tm_min=20, tm_sec=42, tm_wday=4, tm_yday=86, tm_isdst=-1),
    'published_date': time.struct_time((2009, 3, 27, 22, 20, 42, 4, 86, -1)),
    "published": True,
    "comments_link": None,
}


def to_json(python_object):
    if isinstance(python_object, time.struct_time):
        return {'__class__': 'time.asctime',
                '__value__': time.asctime(python_object)}

    if isinstance(python_object, bytes):
        return {'__class__': 'bytes', '__value__': list(python_object)}
    raise TypeError(repr(python_object) + ' is not JSON serializable')


with open('basic.json', mode='w', encoding='utf-8') as f:
    json.dump(basic_entry, f)

with open('basic-bytes.json', mode='w', encoding='utf-8') as f:
    json.dump(basic_entry_bytes, f, default=to_json)

with open('basic-pretty.json', mode='w', encoding='utf-8') as f:
    json.dump(basic_entry, f, indent=2)
