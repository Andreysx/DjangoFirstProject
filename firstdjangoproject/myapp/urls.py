from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='indexmyapp'),
    path('about/', views.about, name='about'),
]
