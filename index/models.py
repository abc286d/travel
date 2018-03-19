from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from slugify import slugify
from ckeditor.fields import RichTextField


class Activity(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    body = RichTextField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)
    show = models.IntegerField(default=1)  # 在什么位置显示，1为当季，2为历史，0为不显示

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
