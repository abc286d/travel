from django.urls import path, re_path
from . import views

app_name = "forum"
urlpatterns = [
    # 帮你开了个头，在这里设计一下论坛每个帖子用什么url，我觉得一串没有意义的数字（数据库里的id）就行了，不需要slug
    # 论坛首页我觉得就用下面这个链接，就是xiniulewan.com/forum/
    # path('', views.activity_list, name='activity_list'),
]