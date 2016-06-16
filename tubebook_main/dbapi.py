from tubebook_main.models import *
import math

PAGE_MAX_POST = 5

class PostList:

    def getPostList(page):
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
            temp = {
                "id": i,
                "title": allPost[i-1].title,
                "author": author.name,
                "author_picture": author.picture_url,
                "date": allPost[i-1].date,
                "video_url": allPost[i-1].video_url,
                "content": allPost[i-1].content,
                "tag": tag.tag_name
            }
            postList.append(temp)


        return postList

    def getPageInfo(page):
        maxpage = math.ceil(Post.objects.count()/PAGE_MAX_POST)
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
    def getTagList():
        allTags = Tag.objects.all()
        return allTags
