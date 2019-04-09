from django.db import models
from django.urls import reverse


# Movies model for data import
class Movie(models.Model):
    # title = models.CharField(max_length=200)
    # url = models.CharField(max_length=200)
    # release_year = models.CharField(max_length=20)

    # vote_count = models.IntegerField()
    # id = models.IntegerField(primary_key=True)
    # video = models.BooleanField(default=False)
    # vote_average = models.DecimalField(decimal_places=1, max_digits=6)
    # title = models.CharField(max_length=200)
    # popularity = models.DecimalField(decimal_places=3, max_digits=7)
    # poster_path = models.FileField()
    # original_language = models.CharField(max_length=10)
    # original_title = models.CharField(max_length=200)
    # # genre_ids = models.CharField(max_length=20)
    # backdrop_path = models.FileField()
    # adult = models.BooleanField(default=False)
    # overview = models.TextField()
    # release_date = models.DateField()
    # price = models.DecimalField(decimal_places=2, max_digits=6)



    """Model representing a movie in the DB
       Arguments:
            models {obj} -- Inherits from Django model class
        """
    genre = models.CharField(max_length=30)
    movie_title = models.CharField(max_length=500)
    movie_logo = models.FileField()
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
