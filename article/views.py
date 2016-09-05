#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext,loader
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.syndication.views import Feed

from .models import Article,Meta


# def index(request):
#     return HttpResponse("this is my article")
def home(request):
    posts = Article.objects.all() #获取全部的Article对象
    paginator = Paginator(posts,2) #每页显示两个
    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request,'article/home.html', {'post_list':post_list})

def detail(request,id):
    try:
        post = Article.objects.get(id = str(id)) #通过 id查找文章具体内容
    except Article.DoesNotExist:
        raise Http404
    return render('request','article/post.html',{'post':post})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render('request','article/archives.html',{'post_list':post_list,'error':False})

def about_me(request):
    return render('request','article/aboutme.html')

def search_tag(request,tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render('request','article/tag.html',{'post_list':post_list})

#Todo 添加blog搜索功能，暂时不加


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - article posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(selfself,item):
        return item.date_time

    def item_description(self, item):
        return item.content


def laboratory(request):
    return render('request','article/laboratory.html')

def sites(request):
    return render('request','article/sites.html')


