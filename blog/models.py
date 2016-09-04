#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)#题目
    category = models.CharField(max_length=50,blank=True)#博客分类标签
    date_time = models.DateTimeField(auto_now_add=True)#博客时间
    content = models.TextField(blank=True,null=True)#博客文章正文,TextField可以表示大量文本
    def __str__(self):
        return self.title


class Meta():
    order = ['-date_time']#按时间倒序排列