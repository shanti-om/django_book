# from django.shortcuts import render
# from .models import Post

# Create your views here.
# def post_list(request):
#     return render(request, 'blog/post_list.html', {})

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
from .templates.blog.menu import main_menu

data = {'menu': main_menu}


def post_list(request):
    data = {'menu': main_menu, 'text': 'post_list', 'posts': Post.published.all()}
    return render(request, 'blog/post/list.html', context=data)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    data = {'menu': main_menu, 'text': 'category_id: ' + str(category_id), 'post': post}
    return render(request, 'blog/post/detail.html', context=data)


def category_id(request, category_id):
    data = {'menu': main_menu, 'text': 'category_id: ' + str(category_id), 'posts': Post.published.all()}
    return render(request, 'blog/post/list.html', context=data)


def category_slug(request, category_slug):
    data = {'menu': main_menu, 'text': 'category_slug: ' + str(category_slug), 'posts': Post.published.all()}
    return render(request, 'blog/post/list.html', context=data)


def about(request):
    data = {'menu': main_menu, 'text': 'about'}
    return render(request, 'blog/about.html', context=data)


def more(request):
    data = {'menu': main_menu, 'text': 'more'}
    return render(request, 'blog/about.html', context=data)
