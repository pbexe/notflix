from django.conf.urls import url
from . import views

app_name = 'users'


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
]