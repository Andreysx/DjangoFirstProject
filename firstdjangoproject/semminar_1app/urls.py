from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/<int:amount_flips>', views.coin, name='coin'),
    path('dice/<int:amount_flips>', views.dice, name='dice'),
    path('number/<int:amount_gens>', views.random_number, name='number'),
    path('result', views.result, name='result'),
]
