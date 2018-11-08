from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse



app_name = 'users'


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(
        r'^login/$',
        auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    url(
        'logout/',
        auth_views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
    url(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='users/password_change.html',
            success_url='users/password-changed',
        ),
        name='change-password'
    ),
    url(
        'password-changed/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='users/password_changed.html',
        ),
        name='password-changed'
    ),
]