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
    url(r'^logout/$', auth_views.logout, {'template_name': 'users/logout.html'}, name='logout'),
    url(r'^signup/$', core_views.signup_view, name='signup'),
]
