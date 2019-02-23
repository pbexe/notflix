from django.contrib import admin
from .models import Movie, Genre

# Add the movie model to the admin DB

class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre', 'slug']
    prepopulated_fields = {'slug': ('genre',)}
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie)
