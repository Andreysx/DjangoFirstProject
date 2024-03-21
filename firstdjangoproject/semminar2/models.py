from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    lastname = models.CharField(max_length=100)
    biography = models.TextField
    date_of_birth = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f"Полное имя {self.name} {self.lastname}"

    def __str__(self):
        return self.full_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_published = models.BooleanField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'Title is {self.title}'
