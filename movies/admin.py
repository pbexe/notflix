from django.contrib import admin
from .models import Movie, Genre, Review, Cluster
from django.core import management
from django.shortcuts import redirect

# Add the movie model to the admin DB

class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre', 'slug']
    prepopulated_fields = {'slug': ('genre',)}
admin.site.register(Genre, GenreAdmin)

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('movie', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

class ClusterAdmin(admin.ModelAdmin):
    model = Cluster
    list_display = ['name', 'get_members']


admin.site.register(Movie)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Cluster, ClusterAdmin)


# admin.site.register(Movie)
