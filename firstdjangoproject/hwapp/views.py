from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer, Product, Order
from datetime import datetime, timedelta
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage
import logging

logger = logging.getLogger(__name__)


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


# Homework 4

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            # created_at = form.created_at['created_at']
            image = form.cleaned_data['image']
            logger.info(f'Получили {name=},'
                        f'{description=},'
                        f'{price= }, {quantity=}.')
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product(name=name, description=description,
                              price=price, quantity=quantity)

            product.save()

    else:
        form = ProductForm()

    return render(request, 'hwapp/add_product.html', {'form': form})


