from django.conf.urls import patterns, include, url


urlpatterns = patterns('blogs.views',
    # url(r'^mysite/', include('mysite.foo.urls')),

    url(r'^$', 'list'),
    url(r'^(?P<blog_id>\d+)/$', 'detail'),

    url(r'^tag/(?P<t_name>\w+)$', 'tag'), # no slash in the end, refer to douban.com

    url(r'^category/(?P<c_id>\d+)/$', 'category'),

    url(r'^about/$', 'about'),
    url(r'^contact/$', 'contact')

)
