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


def post_list(request):
    posts = Post.published.all()
    return render(request,
    'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

def about (request):
    return render(request, 'blog/about.html', {'text': 'Информация о сайте', })
