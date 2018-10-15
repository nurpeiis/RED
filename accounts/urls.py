#this is urls for accounts page, for each user
from django.urls import include,  path
from . import views
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
#accounts is namespace for all the apps in accounts folder
#success_url = post_reset_redirect in django 1.x
app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view (template_name = 'accounts/login.html'), name = 'login'), #login
    path('logout/', LogoutView.as_view (template_name = 'accounts/logout.html'), name = 'logout'), #logout page
    path('register/', views.register, name='register'), #registration
    path('profile/', views.view_profile, name = 'view_profile'),
    path('profile/<int:pk>/', views.view_profile, name = 'view_profile_with_pk'),
    path('profile/edit', views.edit_profile, name = 'edit_profile'),
    path('change-password/', views.change_password, name = 'change_password'),
    path('reset-password/', PasswordResetView.as_view(template_name = 'accounts/reset_password.html', success_url = '/account/reset-password/done/', email_template_name= 'accounts/reset_password_email.html'), name = 'password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name = 'accounts/reset_password_done.html'), name = 'password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = 'accounts/reset_password_confirm.html', success_url = '/account/reset-password/complete/'), name = 'password_reset_confirm'), # it will accept only unique token and uidb64 from the email url 
    path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name = 'accounts/reset_password_complete.html'), name = 'password_reset_complete')
]
