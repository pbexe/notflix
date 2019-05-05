from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from movies.models import Movie


from django.shortcuts import render

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.user.is_authenticated:
        user_id = request.user.id
        current_user_object = User.objects.get(id=user_id)
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = current_user_object
            order = form.save()

            for item in cart:
                OrderItem.objects.create(order=order,
                                         movie=item['movie'],
                                         price=item['price'],)
                # cart.remove(movie=item['movie'])

            # cart.remove(movie=item['movie'])
            cart.clear()

            return render(request, 'order/order/created.html', {'order': order, 'cart': cart})

        else:
            return render(request, 'order/order/create.html', {'form': form})

