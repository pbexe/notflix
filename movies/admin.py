from django.contrib import admin
from .models import Movie, Genre
from django.core import management
from django.shortcuts import redirect

# Add the movie model to the admin DB

class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre', 'slug']
    prepopulated_fields = {'slug': ('genre',)}
admin.site.register(Genre, GenreAdmin)

class MovieAdmin(admin.ModelAdmin):
    @admin.site.register_view('import_movies_from_json_file', 'Import Movies from Json')
    def import_movies_from_url(request):
        print('import movies here')
        try:
            management.call_command('import_from_json_file')
            message = 'successfully imported data from Json file'

        except Exception as ex:
            message = 'Error importing from data from JSON file {}'.format(str(ex))

        admin.ModelAdmin.message_user(Movie, request, message)
        return redirect('admin:index')

admin.site.register(Movie, MovieAdmin)

# admin.site.register(Movie)
