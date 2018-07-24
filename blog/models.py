from django.db import models

class Post(models.Model):

    title       = models.CharField(max_length=120, null=True, blank=True)
    content     = models.TextField(max_length=120, null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):

    commenter = models.CharField(max_length=120, null=False)
    body      = models.TextField(max_length=120, null=True)
    post      = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)