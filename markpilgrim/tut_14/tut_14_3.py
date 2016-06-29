#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request

a_url = 'http://www.diveintopython3.net/examples/feed.xml'
data = urllib.request.urlopen(a_url).read()
print(type(data))
print(data)

