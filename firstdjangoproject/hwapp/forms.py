import datetime
from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=20,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите имя продукта'}))
    description = forms.CharField(max_length=20,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Описание'}))
    price = forms.DecimalField(max_digits=9, decimal_places=2,widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                              'placeholder': 'Цена'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Количество'}))

    # created_at = forms.DateField(initial=datetime.date.today,
    #                              widget=forms.DateInput(attrs={'class': 'form-control'
    #                                  , 'type': 'date'}))
    image = forms.ImageField()
