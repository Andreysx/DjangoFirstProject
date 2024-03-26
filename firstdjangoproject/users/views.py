from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm
from .models import User


# Create your views here.


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('semminar_1app:result')
    #Варгумантах reverse_lazy(по сути пперенаправление) имя приложния и индекс
    template_name = 'users/signup.html'

class MyLoginView(LoginView):
    success_url = reverse_lazy('semminar_1app:result')
    #Варгумантах reverse_lazy(по сути пперенаправление) имя приложния и индекс
    template_name = 'users/signup.html'

    def get_success_url(self):
        return self.success_url
#
# class LogoutView(LogoutView):
#     form_class = CreationForm
#     success_url = reverse_lazy('semminar_1app:result')
#     #Варгумантах reverse_lazy(по сути пперенаправление) имя приложния и индекс
#     template_name = 'users/signup.html'


