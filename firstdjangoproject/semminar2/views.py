from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Author
from .forms import AddNewAuthor, AddNewPost



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

#
# Семминар 4
# Продолжаем работу с авторами, статьями и комментариями.
# Создайте форму для добавления нового автора в базу данных.
# Используйте ранее созданную модель Author


def add_post(request, user_id):
    if request.method == 'POST':
        form = AddNewPost(request.POST)
        if form.is_valid():
            author = Author.objects.get(pk=user_id)
            Post(**form.cleaned_data, author=author).save()
    else:
        form = AddNewPost()
    user = get_object_or_404(Author, pk=user_id)
    posts = Post.objects.filter(author=user)
    context = {
        "title": "Посты",
        "author": user,
        "posts": posts,
        "form": form,
    }
    return render(request, 'semminar2/posts_with_add.html', context)


def add_author(request):
    if request.method == 'POST':
        form = AddNewAuthor(request.POST)
        if form.is_valid():

            Author(**form.cleaned_data).save()
    else:
        form = AddNewAuthor()
    authors = Author.objects.all()
    context = {
        "title": "Авторы",
        "authors": authors,
        "form": form,
    }

    return render(request, 'semminar2/author_add.html', context)