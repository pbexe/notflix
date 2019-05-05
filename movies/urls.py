from django.conf.urls import url

from . import views

app_name = 'movies'

# Regexes of all of the views. The first regex to match the url is then used
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sort_name_asc/$', views.sort_name_asc, name='sort_name_asc'),
    url(r'^sort_name_dsc/$', views.sort_name_dsc, name='sort_name_dsc'),
    url(r'^sort_price_asc/$', views.sort_price_asc, name='sort_price_asc'),
    url(r'^sort_price_dsc/$', views.sort_price_dsc, name='sort_price_dsc'),
    url(r'^sort_date_asc/$', views.sort_date_asc, name='sort_date_asc'),
    url(r'^sort_date_dsc/$', views.sort_date_dsc, name='sort_date_dsc'),
    url(r'^upload/$', views.movie_upload, name='movie_upload'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create_movie/$', views.create_movie, name='create_movie'),
    url(r'^(?P<movie_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^like/$', views.like_movie, name='like_movie'),
    url(r'^dislike/$', views.dislike_movie, name='dislike_movie'),

    url(r'^$', views.review_list, name='review_list'),
    url(r'^movie/(?P<movie_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^recommendation/$', views.user_recommendation_list, name='user_recommendation_list'),

    # ex: /review/5/
    # url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),

    url(r'^(?P<genre_slug>[-\w]+)/$', views.index, name = 'movie_list_by_genre'),


]