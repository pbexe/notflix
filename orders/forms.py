from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Order
import re
import datetime


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('cardholder_name', 'card_number', 'expiry_date', 'CVV_code')



        help_texts = {'expiry_date': "help text", }

    # Validate card_number field.  Usage def clean_<FIELD NAME >, i.e. attributes from
    # the model used for this form

    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']

        # check the user input is only numbers
        if not card_number.isdigit():
            raise forms.ValidationError("Card number can only contain numbers")

        # check the user inputs exactly 16 digits
        elif len(card_number) != 16:
            raise ValidationError('Card must contain 16 digits')

        return card_number

    def clean_CVV_code(self):
        CVV_code = self.cleaned_data['CVV_code']

        # check the user input is only numbers
        if not CVV_code.isdigit():
            raise forms.ValidationError("CVV code can only contain numbers")

        # check the user inputs exactly 3 digits
        elif len(CVV_code) != 3:
            raise ValidationError('CVV code must contain 3 digits')

        return CVV_code

    def clean_cardholder_name(self):
        cardholder_name = self.cleaned_data['cardholder_name']

        # check the user input is only numbers
        if not cardholder_name.replace(" ", "").isalpha():
            raise forms.ValidationError("Card holder name can contain only letters")

        return cardholder_name

    def clean_expiry_date(self):
        expiry_date = self.cleaned_data['expiry_date']

        if not re.match(r'[0-9]{2}/[0-9]{4}', expiry_date):
            raise forms.ValidationError("Date should be in the format MM/YYYY")

        # if not datetime.datetime.strptime(expiry_date, '%m/%Y'):
        #
        #
        #     raise forms.ValidationError("Date should be in the format MM/YYYY")


        return expiry_date



