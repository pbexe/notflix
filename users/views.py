from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse


def signup_view(request):
    """The view that handles sign ups
    
    Arguments:
        request {request} -- The request
    
    Returns:
        render -- The sign up form or a redirect to the index
    """

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            user = form.save()
            login(request, user)
            return redirect('movies:index')
    else:
        form = UserCreationForm()

    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    """The view that handles logins
    
    Arguments:
        request {request} -- The request
    
    Returns:
        render -- The login form or the index is the attempt is successfull
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))


            return redirect('movies:index')

    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    """The view that handles logouts
    
    Arguments:
        request {request} -- The request
    
    Returns:
        render -- The logged out page
    """
    if request.method == 'POST':
        logout(request)
        return render(request, 'users/logout.html')

