#-*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$',views.index,name='index'),
    url(r'^$',views.home,name='home'),
    url(r'(?P<id>\d+)/$',views.detail,name='detail'),
    url(r'^archives/$',views.archives,name='archives'),
    url(r'^aboutme/$',views.about_me,name='about_me'),

]