#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
