from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Author



def index(request):
    return HttpResponse("Hello")


def user_posts(request, user_id):
    user = get_object_or_404(Author, pk=user_id)
    posts = Post.objects.filter(author=user)
    context = {
        "title": "Посты",
        "author": user,
        "posts": posts,
    }
    return render(request, 'semminar2/posts.html', context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.views += 1
    post.save()
    context = {'post': post, }

    return render(request, 'semminar2/post.html', context)