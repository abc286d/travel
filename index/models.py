from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from slugify import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Activity(models.Model):
    title = models.CharField("标题", max_length=200)
    slug = models.SlugField(max_length=500, blank=True)
    body = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    show = models.IntegerField(default=1)  # 在什么位置显示，1为当季，2为历史，0为不显示

    #  图片相关
    image = models.ImageField(upload_to="images/", blank=True)
    url = models.URLField(blank=True)
    slug2 = models.SlugField(max_length=500, blank=True)
    description = models.TextField(default="请在此处填写活动简介")
    departure_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ("title",)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(Activity, self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse("activity:activity_detail", args=[self.id, self.slug])
