from django.contrib.auth.models import Permission, User
from django.db import models
from django.urls import reverse

class Genre(models.Model):
    genre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ('genre',)
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        return reverse('movies:movie_list_by_genre', args=[self.slug])

class Movie(models.Model):
    """Model representing a movie in the DB
    
    Arguments:
        models {obj} -- Inherits from Django model class
    """
    genre = models.ForeignKey(Genre, related_name='movies')
    movie_title = models.CharField(max_length=500)
    movie_logo = models.FileField()
    liked = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)

    #had to create on more field for video for trailer

    def get_absolute_url(self):
        """Absolute url so it can be permalinked
        
        Returns:
            URL -- The absolute URL
        """

        return reverse('movies:detail', args=[self.id])


    def __str__(self):
        """String representation of instance
        
        Returns:
            str -- The title + genre
        """

        return self.movie_title

    def total_likes(self):
        """Returns the total likes of the instance of the movie
        
        Returns:
            int -- Total likes
        """

        return self.likes.count()

    def total_dislikes(self):
        """Returns the total dislikes of the instance of the movie
        
        Returns:
            int -- Total dislikes
        """
        return self.dislikes.count()


class Rental(models.Model):
    """Model of many to many user to movie rental
    
    Arguments:
        models {obj} -- Inherits from the Django model class
    """

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
        """String representation of instance
        
        Returns:
            str -- The renters full name + movie title
        """
        return self.owner.get_full_name() + ": " + self.movie.movie_title
        



