"""
Import json data from JSON file to Datababse
"""
import os
import json
from movies.models import Movie
from django.core.management.base import BaseCommand
from datetime import datetime
from notflix.settings import BASE_DIR


class Command(BaseCommand):
    def import_movie_from_file(self):
        data_folder = os.path.join(BASE_DIR, 'movies', 'resources/json_file')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    movie_title = data_object.get('movie_title', None)
                    genre = data_object.get('genre', None)
                    price = data_object.get('price', None)
                    release_date = data_object.get('release_date', None)
                    description = data_object.get('description', None)

                    try:
                        movie, created = Movie.objects.get_or_create(
                            movie_title=movie_title,
                            genre=genre,
                            price=price,
                            release_date=release_date,
                            description=description

                        )
                        if created:
                            movie.save()
                            display_format = "\nMovie, {}, has been saved."
                            print(display_format.format(movie))
                    except Exception as ex:
                        print(str(ex))
                        msg = "\n\nSomething went wrong saving this movie: {}\n{}".format(movie_title, str(ex))
                        print(msg)


    def handle(self, *args, **options):
        """
        Call the function to import data
        """
        self.import_movie_from_file()

