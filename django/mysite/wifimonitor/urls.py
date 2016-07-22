#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'wifi'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
]