from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^networkaddress/$', views.display, name='display'),
    re_path(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/$', views.display, name='display'),
    re_path(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/delete/$', views.delete, name='delete'),
    re_path(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/add/$', views.add, name='add'),
    re_path(r'^networkaddress/(?P<address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})/modify/$', views.modify, name='modify'),
]
