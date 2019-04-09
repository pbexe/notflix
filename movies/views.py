import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .forms import MovieForm
from .models import Movie, Genre, Like, Dislike
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm
from django.shortcuts import render


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create_movie(request):
    """View used with movie creation
    
    Arguments:
        request {obj} -- The request
    
    Returns:
        render -- Either the movie creation page or the movie details depending
                  on whether the movie has already been created or not
    """

    # Create a form for creating a movie
    form = MovieForm(request.POST or None, request.FILES or None)
    # Check if the submitted form is valid
    if form.is_valid():
        # If it is, take appropriate measures
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
    # If the form isn't valid, ie get request, serve the form.
    return render(request, 'movies/create_movie.html', context)

@login_required(login_url="/users/login")
def detail(request, movie_id):
    """View showing details of a movie. The user must be logged in
    
    Arguments:
        request {obj} -- The request
        movie_id {int} -- The primary key of the movie queried
    
    Returns:
        render -- The details of the movie
    """

    movie = get_object_or_404(Movie, pk=movie_id)
    cart_movie_form = CartAddProductForm()
    is_liked = False
    is_disliked = False

    if Like.objects.filter(user=request.user.id, movie=movie).exists():
        is_liked = True
        is_disliked = False

    if Dislike.objects.filter(user=request.user.id, movie=movie).exists():
        is_disliked = True
        is_liked = False
    return render(request, 'movies/detail.html', {'movie': movie,
                                                  'is_liked': is_liked,
                                                  'is_disliked': is_disliked,
                                                  'total_likes': Like.objects.filter(movie=movie).count(),
                                                  'total_dislikes': Dislike.objects.filter(movie=movie).count(),
                                                  'cart_movie_form': cart_movie_form})

def index(request, genre_slug=None):
    """Directory of the site
    
    Arguments:
        request {request} -- The request
    
    Returns:
        render -- The home page
    """

    genre = None
    genres = Genre.objects.all()
    movies = recommend(request)
    # movies = Movie.objects.filter()
    movie_results = Movie.objects.all()
    query = request.GET.get('q')
    sort_name = request.GET.get('Sort_Name')
    sort_price = request.GET.get('Sort_Price')
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        movies = movies.filter(genre=genre)
    if query:
        movies = movies.filter(
            Q(movie_title__icontains = query)
        ).distinct() or movies.filter(Q(description__icontains=query)).distinct() \
                  or movies.filter(Q(genre__genre__icontains=query)).distinct()  \
                 or movies.filter(Q(release_date__icontains=query)).distinct()

        return render(request, 'movies/index.html', {
            'movies': movies,
        })
    else:
        return render(request, 'movies/index.html', {'genre': genre,
                                                    'genres': genres,
                                                    'movies': movies})


def sort_name_asc(request):
    genre=None
    genres = Genre.objects.all()
    movies = Movie.objects.order_by("movie_title")
    return render(request, 'movies/index.html', {'genre': genre,
                                                 'genres': genres,
                                                 'movies': movies})

def sort_name_dsc(request):
    genre = None
    genres = Genre.objects.all()
    movies = Movie.objects.order_by("-movie_title")
    return render(request, 'movies/index.html', {'genre': genre, 'genres': genres, 'movies': movies})

def sort_price_asc(request):
    genre = None
    genres = Genre.objects.all()
    movies = Movie.objects.order_by("price")
    return render(request, 'movies/index.html', {'genre': genre, 'genres': genres, 'movies': movies})

def sort_price_dsc(request):
    genre = None
    genres = Genre.objects.all()
    movies = Movie.objects.order_by("-price")
    return render(request, 'movies/index.html', {'genre': genre, 'genres': genres, 'movies': movies})

def sort_date_asc(request):
    genre = None
    genres = Genre.objects.all()
    movies = Movie.objects.order_by("release_date")
    return render(request, 'movies/index.html', {'genre': genre, 'genres': genres, 'movies': movies})

def sort_date_dsc(request):
    genre = None
    genres = Genre.objects.all()
    movies = Movie.objects.order_by("-release_date")
    return render(request, 'movies/index.html', {'genre': genre, 'genres': genres, 'movies': movies})


# @permission_required('admin.can.add_log_entry')
def movie_upload(request):
    template = 'movies/movie_upload.html'

    prompt = {
        'order' : 'Order of csv should be first name, last name, email and ip address'
    }
    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']
    #check if it's a csv
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Movie.objects.update_or_create( #contact is the model

          #  "genre", "movie_title", "movie_logo", "id", "description", "release_date", "price"
            genre=column[0],
            movie_title = column[1],
            movie_logo = column[2],
            id = column[3],
            description = column[4],
            release_date = column[5],
            price = column[6]


        )

        context = {}
        return render(request, template, context)




def recommend(request):
    """Dummy recommendation algorithm which returns random movies

    -------- THIS IS NOT A VIEW --------

    Arguments:
        request {obj} -- request information for recommendation
    """ 

    movies = Movie.objects.order_by('?')
    return movies


def favorite(request, movie_id):
    """The view that handles the user favourite request
    
    Arguments:
        request {obj} -- The request
        movie_id {int} -- The id of the movie to favourite
    
    Returns:
        JsonResponse -- A response back to the web page
    """

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
    """The view that handles the user liking the movie
    
    Arguments:
        request {obj} -- The request
    
    Returns:
        HttpResponseRedirect -- Redirect to the liked movie
    """

    movie = get_object_or_404(Movie, id=request.POST.get('movie_id'))
    is_liked = False
    if Like.objects.filter(user=request.user, movie=movie).exists():
        Like.objects.get(user=request.user, movie=movie).delete()
        is_liked = False
    else:
        new = Like(user=request.user, movie=movie)
        new.save()
        if Dislike.objects.filter(user=request.user, movie=movie).count():
            Dislike.objects.get(user=request.user, movie=movie).delete()
        is_liked = True
    return HttpResponseRedirect(movie.get_absolute_url())

def dislike_movie(request):
    """The view that handles the user disliking the movie
    
    Arguments:
        request {obj} -- The request
    
    Returns:
        HttpResponseRedirect -- Redirect to the disliked movie
    """

    movie = get_object_or_404(Movie, id=request.POST.get('movie_id'))
    is_disliked = False
    if Dislike.objects.filter(user=request.user, movie=movie).exists():
        Dislike.objects.get(user=request.user, movie=movie).delete()
        is_disliked = False
    else:
        new = Dislike(user=request.user, movie=movie)
        new.save()
        if Like.objects.filter(user=request.user, movie=movie).count():
            Like.objects.get(user=request.user, movie=movie).delete()
        is_disliked = True
    return HttpResponseRedirect(movie.get_absolute_url())


