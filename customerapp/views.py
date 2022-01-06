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

class PasswordChangeView(views.PasswordChangeView):    
    template_name = 'registration/password_change_form.html'
    success_url = 'profile'

class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'

class PasswordResetView(views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    email_template_name = 'registration/password_reset_email.txt'

class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = 'profile'

class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'






    