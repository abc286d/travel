from django.http import HttpResponse
# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template.loader import get_template

from .models import Post


# Create your views here

def post_list(request):
    posts = Post.objects.all()
    template = get_template('forum/forum.html')

    html = template.render(context=locals(), request=request)

    return HttpResponse(html)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    author_other = Post.objects.filter(author=post.author)
    template = get_template('forum/post.html')

    html = template.render(context=locals(), request=request)

    return HttpResponse(html)
