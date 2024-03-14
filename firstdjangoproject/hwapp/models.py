from django.db import models

# Create your models here.

# Задание
# Создайте три модели Django: клиент, товар и заказ.
#
# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.
#
# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента
#
# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара
#
# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа
#
# Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой базе.


class Customer(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11, blank=False)
    address = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer name: {self.name}, Email: {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product name: {self.name} \n Product price {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order was created at: {self.date_ordered}, Total price = {self.total_price}'
