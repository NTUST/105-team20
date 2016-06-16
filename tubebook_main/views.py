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
