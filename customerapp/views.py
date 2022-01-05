from django.utils.functional import SimpleLazyObject
from django.shortcuts import render
from django.contrib.auth import views
from django.views.generic.detail import DetailView


from .models import Customer
# Create your views here.


class ProfileView(DetailView):
    template_name = 'registration/profile.html'
    model = Customer


    def get_object(self, queryset=None):
        
        if self.request.user.is_authenticated:
            
            """ Словарь для заполнения по умолчанию, если не найден """
            defaults = {
                        'name': self.request.user.username
                        }
            """ Возвращает кортеж (объект, флаг-Истина, если объект создан) """
            customer, created = Customer.objects.get_or_create(user=self.request.user, defaults=defaults)
            return customer
        return None
    

class LoginView(views.LoginView):
    template_name = 'registration/login.html'
    next = 'profile'

class LogoutView(views.LogoutView):
    template_name = 'registration/logged_out.html'
    next_page = 'login'