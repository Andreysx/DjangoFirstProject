from django import forms



class Sem4Task1(forms.Form):
    METHOD_CHOISES = (('Coin', 'Монета'), ('Dice', 'Кубик'), ('Hundred', 'Случайное число от 1 до 100'))

    method = forms.ChoiceField(choices=METHOD_CHOISES)
    count = forms.IntegerField(max_value=64)