#!/usr/bin/python3
# -*- coding: utf-8 -*-


def application(env, start_response):
    """
    Run:
    uwsgi --http :8000 --wsgi-file nginx_test.py
    Test:
    curl localhost:8000
    :param env:
    :param start_response:
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]  # python3
    # return ["Hello World"] # python2
