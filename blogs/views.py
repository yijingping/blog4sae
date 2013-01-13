# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blogs.models import Blog, Tag, Category

PAGE_NUM = 6

def detail(request, blog_id):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_id)
    context['blog'] = blog
    update_context(context)
    return render_to_response('blogs/detail.html', context)

def list(request):
    context = {}
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, PAGE_NUM) 
    page = request.GET.get('page', 1)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)

    context['blogs'] = blogs
    update_context(context)

    return render_to_response('blogs/index.html', context)

def tag(request, t_name=''):
    context = {}
    tag = get_object_or_404(Tag, name=t_name)
    
    blog_list = tag.blogs_with_tag.all()
    paginator = Paginator(blog_list, PAGE_NUM) 
    page = request.GET.get('page', 1)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)
    
    context['blogs'] = blogs
    update_context(context)

    return render_to_response('blogs/index.html', context)


def category(request, c_id='0'):
    context = {}
    category = get_object_or_404(Category, pk=int(c_id))
    
    blog_list = Blog.objects.filter(category=category, author=category.user)
    paginator = Paginator(blog_list, PAGE_NUM) 
    page = request.GET.get('page', 1)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)

    context['blogs'] = blogs
    update_context(context)

    return render_to_response('blogs/index.html', context)

def  update_context(context, user=None):
     context.update({
        'categories': Category.objects.filter(user=user) if user else Category.objects.all(),
        'tags': Tag.objects.all(),
    })

def about(request):
    return render_to_response('blogs/about.html')    

def contact(request):
    return render_to_response('blogs/contact.html')    
    


