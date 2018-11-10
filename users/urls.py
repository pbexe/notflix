from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse



app_name = 'users'


urlpatterns = [

    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]