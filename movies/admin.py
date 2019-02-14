from django.contrib import admin
from .models import Movie

# Add the movie model to the admin DB
admin.site.register(Movie)