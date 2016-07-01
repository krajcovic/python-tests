#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import sys
from http.client import HTTPConnection
from urllib.request import urlopen

import logstash

host = '172.22.17.1'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 4560, version=1))
# test_logger.addHandler(logstash.TCPLogstashHandler(host, 4560, version=1))

test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')

# add extra field to logstash message
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}
test_logger.info('python-logstash: test extra fields', extra=extra)


HTTPConnection.debuglevel = 1
response = urlopen('http://www.diveintopython3.net/examples/feed.xml')
# help(response)
print(response.headers.as_string())
data = response.read()
print(len(data))

response2 = urlopen('http://www.diveintopython3.net/examples/feed.xml')


