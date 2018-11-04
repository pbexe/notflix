from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse


def signup(request):
    """View that processes the user sign up process

    Based on https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
    
    Arguments:
        request {obj} -- The request the user has made
    
    Returns:
        redirect/render -- Redirects user on signup, otherwise renders the view
    """

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('movies:index'))
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})
