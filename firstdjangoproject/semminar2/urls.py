from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/posts', views.user_posts, name='user_posts'),
    path('post/<int:post_id>', views.post, name='post'),
    path('user/<int:user_id>/posts_add', views.add_post, name='posts_and_add'),
    path('authors', views.add_author, name='add_author'),
]
