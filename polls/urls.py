#-*-coding:utf-8-*-
__author__ = 'lqe'

from django.conf.urls import url

from polls.views import Home

urlpatterns = [url(u'^$',Home.as_view(),name='index')]
