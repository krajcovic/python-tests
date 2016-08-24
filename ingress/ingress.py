#!/usr/bin/python3
# -*- coding: utf-8 -*-

import http.cookiejar as cookielib
import json
import requests
from robobrowser import RoboBrowser
import os

GOOGLE_USER = os.getenv('INGRESS_GOOGLE_USER')
GOOGLE_PASS = os.getenv('INGRESS_GOOGLE_PASS')

s = requests.Session()
s.cookies = cookielib.LWPCookieJar()
# cookiejar = cookielib.LWPCookieJar()
# browser = mechanize.Browser()

browser = RoboBrowser(user_agent='TestBot', history=True, session=s)
# browser.set_cookiejar(cookiejar)

browser.open('http://ingress.com/intel')
for link in browser.get_links(url_regex='ServiceLogin'):
    browser.follow_link(link)
    browser.select_form(nr=0)
    browser.form['Email'] = GOOGLE_USER
    browser.form['Passwd'] = GOOGLE_PASS
    browser.submit()

    # req = mechanize.Request('http://www.ingress.com/rpc/dashboard.getGameScore', '{"method": "dashboard.getGameScore"}')
    s2 = requests.Session()
    s2.headers['method'] = 'dashboard.getGameScore'
    for cookie in s.cookies:
        if cookie.name == 'csrftoken':
            # req.add_header('X-CSRFToken', cookie.value)
            s2.headers['X-CSRFToken'] = cookie.value
    s.cookies.add_cookie_header(s2)
    browser = RoboBrowser(session=s2)
    browser.open('http://www.ingress.com/rpc/dashboard.getGameScore')

    # jsonData = '\n'.join(mechanize.urlopen(req).readlines())
    # print(json.loads(jsonData))

# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod()
