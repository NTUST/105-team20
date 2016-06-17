from django.shortcuts import render_to_response
from tubebook_main.dbapi import *

def firstindex(request):
    return index(request, 1)

def index(request, page):
    try:
        posts = PostList.getPostList(page)
        sidePosts = PostList.getPostList(1)
        page = PostList.getPageInfo(page)
        tages = TagList.getTagList()

        return render_to_response('index.html', locals())
    except:
        sidePosts = PostList.getPostList(1)
        page = PostList.getPageInfo(page)
        tages = TagList.getTagList()
        return render_to_response('404.html', locals())

def post(request, id):
    try:
        post = PostList.getPost(id)
        return render_to_response('post.html', locals())
    except:
        sidePosts = PostList.getPostList(1)
        page = PostList.getPageInfo(page)
        tages = TagList.getTagList()
        return render_to_response('404.html', locals())


def about(request):
    try:
        return render_to_response('about.html', locals())
    except:
        sidePosts = PostList.getPostList(1)
        page = PostList.getPageInfo(page)
        tages = TagList.getTagList()
        return render_to_response('404.html', locals())


def authorList(request):
    try:
        authors = Authors.getAuthorList()
        return render_to_response('author.html', locals())
    except:
        sidePosts = PostList.getPostList(1)
        page = PostList.getPageInfo(page)
        tages = TagList.getTagList()
        return render_to_response('404.html', locals())


def authorProfile(request, id):
    try:
        author = Authors.getAuthorProfile(id)
        posts = PostList.getPostList(1, "author", id)
        return render_to_response('author_profile.html', locals())
    except:
        sidePosts = PostList.getPostList(1)
        page = PostList.getPageInfo(page)
        tages = TagList.getTagList()
        return render_to_response('404.html', locals())


def postListByTag(request, id, page):
    try:
        posts = PostList.getPostList(page, "tag", id)
        sidePosts = PostList.getPostList(1)
        page = PostList.getPageInfo(page, "tag", id)
        tages = TagList.getTagList()
        tag = TagList.getTag(id)

        return render_to_response('tag_post.html', locals())
    except:
        sidePosts = PostList.getPostList(1)
        page = PostList.getPageInfo(page)
        tages = TagList.getTagList()
        return render_to_response('404.html', locals())


def postListByAuthor(request, id, page):
    try:
        posts = PostList.getPostList(page, "author", id)
        sidePosts = PostList.getPostList(1)
        page = PostList.getPageInfo(page, "author", id)
        tages = TagList.getTagList()
        author = Authors.getAuthorProfile(id)

        return render_to_response('author_post.html', locals())
    except:
        sidePosts = PostList.getPostList(1)
        page = PostList.getPageInfo(page)
        tages = TagList.getTagList()
        return render_to_response('404.html', locals())
