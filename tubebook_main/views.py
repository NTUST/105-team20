from django.shortcuts import render_to_response
from tubebook_main.dbapi import *

def firstindex(request):
    return index(request, 1)

def index(request, page):
    posts = PostList.getPostList(page)
    sidePosts = PostList.getSidePostList()
    page = PostList.getPageInfo(page)
    tages = TagList.getTagList()

    return render_to_response('index.html', locals())

def post(request, id):
    post = PostList.getPost(id)
    return render_to_response('post.html', locals())

def about(request):
    return render_to_response('about.html', locals())

def authorList(request):
    authors = Authors.getAuthorList()
    return render_to_response('author.html', locals())
