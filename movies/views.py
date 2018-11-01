
from django.shortcuts import render, get_object_or_404
from .forms import MovieForm
from .models import Movie
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponseRedirect




from django.shortcuts import render

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']



def create_movie(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        movie = form.save(commit=False)
        #movie.user = request.user
        movie.movie_logo = request.FILES['movie_logo']

        file_type = movie.movie_logo.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'movie': movie,
                'form': form,
                'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
            return render(request, 'movies/create_movie.html', context)
        movie.save()
        return render(request, 'movies/detail.html', {'movie': movie})
    context = {
        "form": form,
    }
    return render(request, 'movies/create_movie.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    is_liked = False
    if movie.likes.filter(id=request.user.id).exists():
        is_liked = True
    return render(request, 'movies/detail.html', {'movie': movie,
                                                  'is_liked': is_liked,
                                                  'total_likes': movie.total_likes()})

def index(request):
    movies = Movie.objects.filter()
    movie_results = Movie.objects.all()
    query = request.GET.get('q')
    if query:
        movies = movies.filter(
            Q(movie_title__icontains = query)
        ).distinct()

        return render(request, 'movies/index.html', {
            'movies': movies,
        })
    else:
        return render(request, 'movies/index.html', {'movies': movies})

def favorite(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    try:
        if movie.liked:
            movie.liked = False
        else:
            movie.liked = True
        movie.save()
    except (KeyError, Movie.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})



def like_movie(request):
    movie = get_object_or_404(Movie, id=request.POST.get('movie_id'))
    is_liked = False
    if movie.likes.filter(id=request.user.id).exists():
        movie.likes.remove(request.user)
        is_liked = False
    else:
        movie.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(movie.get_absolute_url())








