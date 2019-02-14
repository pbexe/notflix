from django.conf.urls import url
from . import views

app_name = 'movies'

# Regexes of all of the views. The first regex to match the url is then used
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create_movie/$', views.create_movie, name='create_movie'),
    url(r'^(?P<movie_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^like/$', views.like_movie, name='like_movie'),
    url(r'^dislike/$', views.dislike_movie, name='dislike_movie'),

]