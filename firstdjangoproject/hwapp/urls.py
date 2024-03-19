from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('customer/<int:customer_id>/<int:days>', views.list_of_products_by_date, name='customer_days'),
]
