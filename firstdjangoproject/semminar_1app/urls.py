from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/<int:amount_flips>', views.coin, name='coin'),
    path('dice/', views.dice, name='dice'),
    path('number/', views.random_number, name='number'),
]
