from django.conf.urls import url

from . import views

app_name = 'stats'

# Regexes of all of the views. The first regex to match the url is then used
urlpatterns = [
    url(r'^$', views.main, name='main'),
]