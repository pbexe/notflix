from django import forms
from django.contrib.auth.models import User

from .models import Movie


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['movie_title', 'genre', 'movie_logo', 'description', 'release_date']

