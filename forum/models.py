# coding:utf-8
import datetime

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from account.models import UserProfile


class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField("images", upload_to="images/")
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = u'主题'

    def __unicode__(self):
        return self.title

    def description(self):
        return u'%s 发表了主题《%s》' % (self.author, self.title)

    def get_absolute_url(self):
        return "/forum/post_detial/%i/" % self.id



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = u'评论'

    def __unicode__(self):
        return self.content

    def description(self):
        return u'%s 回复了您的帖子(%s) R:《%s》' % (self.author, self.post, self.content)


class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likesCount = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.likesCount
