from django.conf.urls import url
import home.views

urlpatterns = [
    url('^$',home.views.AboutView.as_view(), name='index'),
]