from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponse
from movies.models import Movie, Like, Dislike


# Create your views here.
def main(request):
    if request.user.is_superuser:
        context = {}
        context['number'] = Movie.objects.all().count()
        context['likes'] = Like.objects.all().count()
        context['dislikes'] = Dislike.objects.all().count()

        return render(request, 'stats/main.html', context=context)
    else:
        return HttpResponseNotAllowed("Hello there")

