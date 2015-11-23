from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class AboutView(TemplateView):
    template_name = "home/about.html"

    def get_context_data(self, **kwargs):
        data = super(AboutView,self).get_context_data(**kwargs)
        data['home_name']='lqe.home'
        return data

