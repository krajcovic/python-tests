#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.parse import urlencode
import httplib2

httplib2.debuglevel = 1

data = {'status': 'Test update from Python 3'}
print(urlencode(data))

