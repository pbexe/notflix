from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from movies.models import Review

from .models import Movie


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['movie_title', 'genre', 'movie_logo', 'description', 'release_date']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }