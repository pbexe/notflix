from django.contrib.auth.models import Permission, User
from django.db import models

class Movie(models.Model):
    movie_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    movie_logo = models.FileField()
    liked = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField()

    def __str__(self):
        return self.movie_title + '-' + self.genre




