# -*- coding: utf-8 -*-
from django.utils.html import strip_tags
from BeautifulSoup import NavigableString, BeautifulSoup

def filter_html(src):
    # step 1: 过滤html标签
    flat_src = strip_tags(src)
    # step 2：处理未闭合的标签
    p = BeautifulSoup(flat_src)
    text = p.findAll(text=lambda text:isinstance(text, NavigableString))

    return u" ".join(text)