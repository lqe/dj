__author__ = 'Administrator'

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns=[
    url(u'^index$',TemplateView.as_view(template_name="blog/index.html"))
]
