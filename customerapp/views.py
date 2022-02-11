from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views
from django.views.generic.detail import DetailView

from allauth.account.views import LoginView, SignupView
from allauth.account.utils import passthrough_next_redirect_url, get_request_param
from django.contrib.sites.shortcuts import get_current_site

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


class CustomLoginView(LoginView):

	def get_context_data(self, **kwargs):

		ret = super(LoginView, self).get_context_data(**kwargs)
		signup_url = passthrough_next_redirect_url(self.request,reverse('account_signup'),self.redirect_field_name)

		redirect_field_value = get_request_param(self.request,self.redirect_field_name)
		site = get_current_site(self.request)

		ret.update({'signup_url': signup_url,
                    'site': site,
                    'redirect_field_name': self.redirect_field_name,
                    'redirect_field_value': redirect_field_value,
        			})

		return ret

class CustomSignupView(SignupView):

	def get_context_data(self, **kwargs):
		ret = super(SignupView, self).get_context_data(**kwargs)

		form = ret['form']
		email = self.request.session.get('account_verified_email')

		if email:
			email_keys = ['email']
			if app_settings.SIGNUP_EMAIL_ENTER_TWICE:
				email_keys.append('email2')
			for email_key in email_keys:
				form.fields[email_key].initial = email

		login_url = passthrough_next_redirect_url(self.request,reverse("account_login"),self.redirect_field_name)
		redirect_field_name = self.redirect_field_name
		redirect_field_value = get_request_param(self.request,redirect_field_name)

		ret.update({'login_url': login_url,
	                'redirect_field_name': redirect_field_name,
	                'redirect_field_value': redirect_field_value,
	                })
		return ret