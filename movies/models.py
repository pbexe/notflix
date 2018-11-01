from django.contrib.auth.models import Permission, User
from django.db import models
from django.urls import reverse


class Movie(models.Model):
    movie_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    movie_logo = models.FileField()
    liked = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    #had to create on more field for video for trailer

    def get_absolute_url(self):
        return reverse('movies:detail', args=[str(self.id)])


    def __str__(self):
        return self.movie_title + '-' + self.genre


class Rental(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )
    expiration = models.DateTimeField()

    def __str__(self):
        return self.owner.get_full_name() + ": " + self.movie.movie_title 
        



