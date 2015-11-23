#-*- coding:utf-8 -*-
import django
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
class Home(object):

    def __init__(self):
        pass

    @classmethod
    def as_view(cls):
        template = loader.get_template('index.html')
        return HttpResponse('ok')