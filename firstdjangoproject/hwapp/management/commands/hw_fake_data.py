from django.core.management.base import BaseCommand
from hwapp.models import Customer, Product, Order

class Command(BaseCommand):
    help = "Generate fake customers, products, orders"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Amount of fake data')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            customer = Customer(name=f'Name{i}',
                                email=f'fake_em{i}mail.ru',
                                phone_number=f'+7934123234{i}',
                                address=f'Fake adress{i}'
                                )
            customer.save()
            for j in range(1, count + 1):
                product = Product(name=f'Name{i}', price=f'1234.3{i}', quantity=f'{i}')
                product.save()
                for k in range(1, count + 1):
                    order = Order(customer=customer)
                    order.save()

