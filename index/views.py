from django.shortcuts import render, get_object_or_404
from .models import Activity


def index(request):
    hotdeals = Activity.objects.filter(show=1, show2=1)
    retrospections = Activity.objects.filter(show=2, show2=1)
    return render(request, 'index/index.html', {"hotdeals": hotdeals, "retrospections": retrospections})


def activity_list(request):
    activities = Activity.objects.all()
    return render(request, "index/activity_list.html", {"activities": activities})


def retrospection_list(request):
    activities = Activity.objects.all()
    return render(request, "index/retrospection_list.html", {"activities": activities})


def activity_detail(request, id, slug):
    activity = get_object_or_404(Activity, id=id, slug=slug)
    return render(request, "index/activity_detail.html", {"activity": activity})
