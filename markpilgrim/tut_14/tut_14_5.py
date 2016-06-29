#!/usr/bin/python3
# -*- coding: utf-8 -*-

import httplib2

httplib2.debuglevel = 1
h = httplib2.Http('.cache')

print('*** Response 1 ***')
response, content = h.request('http://www.diveintopython3.net/examples/feed.xml')
print(response.status)
# print(content[:52])
print(len(content))
print(response.fromcache)


print('*** Response 2 ***')
response2, content2 = h.request('http://www.diveintopython3.net/examples/feed.xml', headers={'cache-control': 'no-cache'})
print(response2.status)
print(len(content2))
print(response2.fromcache)