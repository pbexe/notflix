from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponse


# Create your views here.
def main(request):
    if request.user.is_superuser:
        return render(request, 'stats/main.html')
    else:
        return HttpResponseNotAllowed("Hello there")

