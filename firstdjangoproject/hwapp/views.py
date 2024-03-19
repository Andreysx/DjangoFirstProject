from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer, Product, Order
from datetime import datetime, timedelta


def index(request):
    return HttpResponse('Hello Django')


def list_of_products_by_date(request, customer_id: int, days: int):
    date = datetime.now() - timedelta(days=days)
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer, date_ordered=date)
    # products = [order.get_products() for order in orders]
    names = []
    for order in orders:
        products = order.get_products()
        for product in products:
            names.append(product.name)
            print(product.name)

    context = {
        'customer': customer.name,
        'products': names,
        'days': days
    }
    return render(request, 'hwapp/hwfile.html', context)