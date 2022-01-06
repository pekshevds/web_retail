from django.urls import path
from .views import LoginView, LogoutView, ProfileView, PasswordChangeView, \
    PasswordChangeDoneView, PasswordResetView, PasswordResetCompleteView,\
         PasswordResetConfirmView, PasswordResetDoneView


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),

    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
]