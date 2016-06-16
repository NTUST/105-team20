from django.db import models

class WriterAccount(models.Model):
    account = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

class WriterProfile(models.Model):
    name = models.CharField(max_length = 30)
    picture_url = models.CharField(max_length = 100)
    mail = models.CharField(max_length = 50)
    about = models.TextField()

class Post(models.Model):
    author_id = models.IntegerField()
    tag_id = models.IntegerField()
    title = models.CharField(max_length = 100)
    video_url = models.CharField(max_length = 100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

class Tag(models.Model):
    tag_name = models.CharField(max_length = 30)
