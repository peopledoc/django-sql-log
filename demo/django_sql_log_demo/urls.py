from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url('^500/', views.raise_exception),
]
