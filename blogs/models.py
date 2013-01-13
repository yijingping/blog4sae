# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from django.db import models
from tinymce.models import HTMLField
from . import util

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='标签名', unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified = models.DateTimeField(auto_now=True, verbose_name='修改时间')    

    def __unicode__(self):
        return self.name

    @property
    def list_url(self):
        return '/tag/%s'%self.name
        
    class Meta:
        verbose_name = '标签'

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='类别名', unique=True)
    user = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    
    def __unicode__(self):
        return self.name

    @property
    def list_url(self):
        return '/category/%s/'%self.id

    class Meta:
        verbose_name = '类别'

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    author = models.ForeignKey('auth.User')
    content = HTMLField(verbose_name='内容')
    category = models.ForeignKey('Category')
    tags = models.ManyToManyField(Tag, related_name='blogs_with_tag', db_table='blogs_blog_tag')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    
    def __unicode__(self):
        return self.title

    @property
    def detail_url(self):
        return '/blogs/%s/'%self.id
    @property
    def brief(self):
        brief = util.filter_html(self.content) if self.content else ""
        return brief[:100]

    class Meta:
        verbose_name = '博客'

