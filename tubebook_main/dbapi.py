from tubebook_main.models import *
import math

PAGE_MAX_POST = 5

class PostList:

    def getPost(id):
        post_id = int(id)
        post = Post.objects.get(id = post_id)
        author = WriterProfile.objects.get(id = post.author_id)
        tag = Tag.objects.get(id = post.tag_id)
        return {
            "id": id,
            "title": post.title,
            "author": author.name,
            "author_id": post.author_id,
            "author_picture": author.picture_url,
            "date": post.date,
            "video_url": post.video_url,
            "content": post.content,
            "tag_id": post.tag_id,
            "tag": tag.tag_name
        }

    def getSidePostList():
        firstPost = Post.objects.count()
        postList = []

        for i in range(firstPost, firstPost-6, -1):
            post = Post.objects.get(id = i)
            author = WriterProfile.objects.get(id = post.author_id)

            temp = {
                "id": i,
                "title": post.title,
                "author_picture": author.picture_url,
                "date": post.date
            }
            postList.append(temp)

        return postList

    def getAuthorPost(id, page):
        author_id = int(id)
        pageNum = int(page)

        author = WriterProfile.objects.get(id = author_id)
        posts = Post.objects.filter(author_id = author_id)
        count = posts.count()
        result = []

        firstPost = count - PAGE_MAX_POST * (pageNum - 1)
        lastPost = firstPost - PAGE_MAX_POST
        if lastPost < 1 :
            lastPost = 1

        for i in range(firstPost, lastPost-1, -1):
            tag = Tag.objects.get(id = posts[i-1].tag_id)
            content = posts[i-1].content
            if len(content) > 120:
                content = content[:120]
            temp = {
                "id": posts[i-1].i,
                "title": posts[i-1].title,
                "author": author.name,
                "author_id": posts[i-1].author_id,
                "author_picture": author.picture_url,
                "date": posts[i-1].date,
                "video_url": posts[i-1].video_url,
                "content": content,
                "tag_id": posts[i-1].tag_id,
                "tag": tag.tag_name
            }
            result.append(temp)

        return result

    def getPostList(page, type="", id=""):
        pageNum = int(page)
        if type == "tag":
            posts = Post.objects.filter(tag_id = int(id))
        elif type == "author":
            posts = Post.objects.filter(author_id = int(id))
        else:
            posts = Post.objects.all()

        count = posts.count()
        firstPost = count - PAGE_MAX_POST * (pageNum - 1)
        lastPost = firstPost - PAGE_MAX_POST
        if lastPost < 0 :
            lastPost = 0

        posts = posts[lastPost:firstPost]
        result = []
        for post in posts:
            author = WriterProfile.objects.get(id = post.author_id)
            tag = Tag.objects.get(id = post.tag_id)
            content = post.content
            if len(content) > 120:
                content = content[:120]
            temp = {
                "id": post.id,
                "title": post.title,
                "author": author.name,
                "author_id": post.author_id,
                "author_picture": author.picture_url,
                "date": post.date,
                "video_url": post.video_url,
                "content": content,
                "tag_id": post.tag_id,
                "tag": tag.tag_name
            }

            result.insert(0, temp)
        return result

    def getAllPostList(page):
        pageNum = int(page)
        allPost = Post.objects.all()
        firstPost = Post.objects.count() - PAGE_MAX_POST * (pageNum - 1)
        lastPost = firstPost - PAGE_MAX_POST
        if lastPost < 1 :
            lastPost = 1
        postList = []

        for i in range(firstPost, lastPost-1, -1):
            author = WriterProfile.objects.get(id = allPost[i-1].author_id)
            tag = Tag.objects.get(id = allPost[i-1].tag_id)
            content = allPost[i-1].content
            if len(content) > 120:
                content = content[:120]
            temp = {
                "id": i,
                "title": allPost[i-1].title,
                "author": author.name,
                "author_id": allPost[i-1].author_id,
                "author_picture": author.picture_url,
                "date": allPost[i-1].date,
                "video_url": allPost[i-1].video_url,
                "content": content,
                "tag_id": allPost[i-1].tag_id,
                "tag": tag.tag_name
            }
            postList.append(temp)


        return postList

    def getPageInfo(page, type="index", id=""):
        if type == "index":
            maxpage = math.ceil(Post.objects.count()/PAGE_MAX_POST)
        elif type == "tag":
            tag_id = int(id)
            maxpage = math.ceil(Post.objects.filter(tag_id = tag_id).count()/PAGE_MAX_POST)
        elif type == "author":
            author_id = int(id)
            maxpage = math.ceil(Post.objects.filter(author_id = author_id).count()/PAGE_MAX_POST)


        emN = False
        if (int(page) + 1 > maxpage ):
            emN = True

        emP = False
        if (int(page) - 1 <= 0 ):
            emP = True

        return {
            "next": int(page) + 1,
            "previous": int(page) - 1,
            "emN": emN,
            "emP": emP
        }

class TagList:
    def getTag(id):
        tag_id = int(id)
        tag = Tag.objects.get(id = tag_id)
        return {
            "id": tag.id,
            "name": tag.tag_name
        }

    def getTagList():
        allTags = Tag.objects.all()
        return allTags

class Authors:
    def getAuthorProfile(id):
        author_id = int(id)
        author = WriterProfile.objects.get(id = author_id)
        count = Post.objects.filter(author_id = author_id).count()
        return {
            "id": author.id,
            "name": author.name,
            "picture_url": author.picture_url,
            "mail": author.mail,
            "about": author.about,
            "count": count
        }

    def getAuthorList():
        allAuthor = WriterProfile.objects.all()
        result = []
        for author in allAuthor:
            temp = {
                "id": author.id,
                "name": author.name,
                "picture_url": author.picture_url
            }
            result.append(temp)

        return result
