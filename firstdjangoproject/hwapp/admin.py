from django.contrib import admin
from .models import Customer, Product, Order
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    #настройка отображения
    list_display = ['name', 'email', 'phone_number', 'address']
    #добавление фильтрации
    list_filter = ['created_at']
    list_editable = ['email', 'phone_number']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'description']
    # добавление фильтрации
    list_filter = ['created_at', 'price', 'quantity']
    #То есть поля, перечисленные в, list_editableбудут отображаться в виде виджетов
    # формы на странице списка изменений, что позволит пользователям редактировать и сохранять несколько строк одновременно
    list_editable = ['description']
    #Поиск по полю
    search_fields = ['description']
    #текст
    search_help_text = 'Поиск по полю Описание продукта (description)'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'date_ordered']
    list_editable = ['total_price']
    list_filter = ['total_price', 'date_ordered']
