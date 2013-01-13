# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from blogs.models import Blog, Tag, Category
from django.contrib import admin

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created','modified',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created','modified',)

class BlogAdmin(admin.ModelAdmin):
    def title_with_link(self):
        return "<a href=\"%s\" target=\"_blank\">%s</a>"%(self.detail_url, self.title)
    title_with_link.short_description='标题'
    title_with_link.allow_tags=True

    list_display = ('id', title_with_link, 'author', 'brief', 'category', 'created','modified',)
    search_fields = ('title', 'content')
    list_filter = ('category__name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)