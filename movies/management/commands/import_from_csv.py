"""
Import json data from CSV file to Datababse
"""
import os
import csv
from movies.models import Movie
from django.core.management.base import BaseCommand
from datetime import datetime
from notflix.settings import BASE_DIR


class Command(BaseCommand):
    def import_movie_from_csv_file(self):
        data_folder = os.path.join(BASE_DIR, 'movies', 'resources/csv_file')
        print(data_folder, 'data_folder')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = csv.reader(data_file)
                for data_object in data:
                    # title = data_object[2]
                    # url = data_object[3]
                    # release_year = datetime.now()

                    genre = data_object[0],
                    movie_title = data_object[1],
                    movie_logo = data_object[2],
                    id = data_object[3],
                    description = data_object[4],
                    release_date = data_object[5],
                    price = data_object[6]

                    try:
                        movie, created = Movie.objects.get_or_create(
                            # title=title,
                            # url=url,
                            # release_year=release_year
                            genre=genre,
                            movie_title=movie_title,
                            movie_logo=movie_logo,
                            id=id,
                            description=description,
                            release_date=release_date,
                            price=price



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
        self.import_movie_from_csv_file()

