from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    SEX_CHOICES = (
        ("M", "男"),
        ("F", "女"),
    )

    user = models.OneToOneField(User, models.CASCADE, unique=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default="F", blank=True)
    address = models.CharField(max_length=10, blank=True)
    aboutme = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
