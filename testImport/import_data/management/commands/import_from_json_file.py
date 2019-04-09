"""
Import json data from JSON file to Datababse
"""
import os
import json
from import_data.models import Movie
from django.core.management.base import BaseCommand
from datetime import datetime
from testImport.settings import BASE_DIR


class Command(BaseCommand):
    def import_movie_from_file(self):
        data_folder = os.path.join(BASE_DIR, 'import_data', 'resources/json_file')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                for data_object in data:
                    # title = data_object.get('title', None)
                    # url = data_object.get('url', None)
                    # release_year = datetime.now()

                    # vote_count = data_object.get('vote_count', None)
                    # id = data_object.get('id', None)
                    # video = data_object.get('video', None)
                    # vote_average = data_object.get('vote_average', None)
                    # title = data_object.get('title', None)
                    # popularity = data_object.get('popularity', None)
                    # poster_path = data_object.get('poster_path', None)
                    # original_language = data_object.get('original_language', None)
                    # original_title = data_object.get('original_title', None)
                    # genre_ids = data_object.get('genre_ids', None)
                    # backdrop_path = data_object.get('backdrop_path', None)
                    # adult = data_object.get('adult', None)
                    # overview = data_object.get('overview', None)
                    # release_date = data_object.get('release_date', None)
                    # price = data_object.get('price', None)

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
                            # title=title,
                            # url=url,
                            # release_year=release_year

                            # vote_count=vote_count,
                            # id=id,
                            # video = video,
                            # vote_average=vote_average,
                            # title=title,
                            # popularity=popularity,
                            # poster_path=poster_path,
                            # original_language=original_language,
                            # original_title=original_title,
                            # genre_ids=genre_ids,
                            # backdrop_path=backdrop_path,
                            # adult=adult,
                            # overview=overview,
                            # release_date=release_date,
                            # price=price

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

