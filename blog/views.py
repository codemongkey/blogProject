# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Post,Category
from comments.forms import CommentForm
import markdown
def index(request):
    print '111'
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})
    
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 记得在顶部引入 markdown 模块
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)
    
    
def archives(request, year, month):
    post_list = Post.objects.all().filter(created_time__year=year,
                                          created_time__month=month
                                          )
    return render(request, 'blog/index.html', context={'post_list': post_list})
def category(request, pk):
    # 记得在开始部分导入 Category 类
    print pk
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    