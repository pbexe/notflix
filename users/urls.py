"""Authenitcation URLs
"""

from django.conf.urls import url, include
from . import views
from . import views as core_views
from django.contrib.auth import views as auth_views
from django.urls import reverse

app_name = 'users'

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', core_views.signup_view, name='signup'),
    url(r'^details/$', views.detail_view, name='details'),
    url(r'^password/$', views.change_password, name='change_password'),

]
