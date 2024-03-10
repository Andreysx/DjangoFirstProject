from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/', views.coin, name='index'),
    path('dice/', views.dice, name='about'),
    path('number/', views.random_number, name='about'),
]
