from django import forms
import datetime
from .models import Author


class AddNewAuthor(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    lastname = forms.CharField(max_length=100)
    # biography = forms.CharField(widget=forms.Textarea)
    date_of_birth = forms.DateField(initial=datetime.date.today,
                                    widget=forms.DateInput(attrs={'class': 'form-control'
                                        , 'type': 'date'}))


class AddNewPost(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    # date = forms.DateField(initial=datetime.date.today,
    #                        widget=forms.DateInput(attrs={'type': 'date'}))
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    is_published = forms.BooleanField()
    # views = forms.IntegerField()

# Author.objects.all() - queryset
