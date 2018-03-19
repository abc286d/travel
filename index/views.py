from django.shortcuts import render,get_object_or_404
from .models import Activity


def index(request):
    return render(request, 'index/index.html')


def activity_list(request):
    activities = Activity.objects.all()
    return render(request, "index/activity_list.html", {"activities": activities})


def activity_detail(request, id, slug):
    activity = get_object_or_404(Activity, id=id, slug=slug)
    return render(request, "index/activity_detail.html", {"activity": activity})
