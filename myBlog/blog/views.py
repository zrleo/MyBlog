#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext,loader

from .models import Article,Meta


def index(request):
    return HttpResponse("this is my blog")
