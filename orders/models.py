from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from movies.models import Movie


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    card_number = models.CharField(max_length=16)
    cardholder_name = models.CharField(max_length=50)
    # expiry_date = models.CharField(max_length=10, help_text="MM/YYYY")
    CVV_code = models.CharField(max_length=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    expiry_date_month = models.IntegerField(default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)])
    expiry_date_year = models.IntegerField(default=2020,
        validators=[MaxValueValidator(2030), MinValueValidator(2019)])
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='item', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='order_item', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price