from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from slugify import slugify


class Activity(models.Model):
    title = models.CharField("标题", max_length=200)
    image = models.ImageField('活动主图', upload_to="images/")
    departure_date = models.DateField('活动时间', default=timezone.now)
    description = models.TextField(default="请在此处填写活动简介，此简介将显示在首页")
    description2 = models.TextField(default="请在此处填写活动简介，此简介将展示在活动列表页面")
    body = models.TextField(default='请在此处添加具体文章')

    SHOW_CHOICES = (
        (1, "当季热卖"),
        (2, "历史活动"),
        (3, '不显示在活动列表中'),
    )
    SHOW2_CHOICES = (
        (1, '是'),
        (2, "否"),
    )

    show = models.IntegerField('活动类型', choices=SHOW_CHOICES, default=1)
    show2 = models.IntegerField("是否显示在首页", choices=SHOW2_CHOICES, default=1)

    slug = models.SlugField('不用填写', max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-updated",)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(Activity, self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse("activity:activity_detail", args=[self.id, self.slug])
