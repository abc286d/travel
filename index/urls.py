from django.urls import path, re_path
from . import views

app_name = "activity"
urlpatterns = [
    path('activity_list/', views.activity_list, name='activity_list'),
    re_path(r'^activity_detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.activity_detail, name='activity_detail')
]
