# adpated from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

FAVORITE_GENRE_CHOICES = (
    ('comedy', 'Comedy'),
    ('horror', 'Horror'),
    ('all', 'All'),
)


class DateInput(forms.DateInput):
    input_type = 'date'

class ChoiceInput(forms.ChoiceField):
    input_type = 'choice'

class SignUpForm(UserCreationForm):

    address = forms.CharField(max_length=250)
    city = forms.CharField(max_length=30)
    postcode = forms.CharField(max_length=30, help_text='postcode field')
    date_birth = forms.DateField()
    # preferred_genre = forms.ChoiceField(choices=FAVORITE_GENRE_CHOICES, widget=forms.RadioSelect)

    # date_birth=fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'address',
                  'city', 'postcode', )
        widgets = {
            'date_birth': DateInput(),
            # 'preferred_genre': ChoiceInput()

        }
