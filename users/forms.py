# adpated from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    address = forms.CharField(max_length=250)
    city = forms.CharField(max_length=30)
    postcode = forms.CharField(max_length=30, help_text='postcode field')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'address',
                  'city', 'postcode')
