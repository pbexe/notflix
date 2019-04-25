from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from movies.models import Movie
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, movie_id):
    cart = Cart(request)
    movie = get_object_or_404(Movie, id=movie_id)
    form = CartAddProductForm(request.POST)

    # if movie_id in cart.cart.get(movie_id):
    #     return redirect('cart:cart_detail')

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(movie=movie)
                 #quantity=cd['quantity'],
                 #update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, movie_id):
    cart = Cart(request)
    movie = get_object_or_404(Movie, id=movie_id)
    cart.remove(movie)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    #for item in cart:
    #    item['update_quantity_form'] = CartAddProductForm(initial={#'quantity': item['quantity'],
    #                                                               'update': True})
    return render(request, 'cart/detail.html', {'cart': cart, 'cartlength': len(cart)})

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')
