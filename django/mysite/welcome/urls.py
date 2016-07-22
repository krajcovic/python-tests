#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'welcome'
urlpatterns = [
    # ex: /index/
    url(r'^$', TemplateView.as_view(template_name='welcome/index.html'), name='index')
]
