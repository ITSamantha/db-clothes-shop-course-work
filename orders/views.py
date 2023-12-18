import json
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

import dictionaries.topics
import orders.utils
import products.utils
from orders.models import Cart
from products.models import Category, ProductSizeColor


# Create your views here.

def cart(request):
    categories = Category.objects.all()

    return render(request, 'orders/cart.html')


class CartView(ListView):
    template_name = 'orders/cart.html'
    model = Cart
    context_object_name = 'products'

    def get_queryset(self):
        return orders.utils.get_cart_products(self.request.user)


class CheckoutView(TemplateView):
    template_name = 'orders/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class FavouritesView(TemplateView):
    template_name = 'orders/favourites.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def add_product_to_cart(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        count = int(data.get('count'))
        product = int(data.get('product'))
        product_size_color = get_object_or_404(ProductSizeColor, id=product)

        cart = Cart.objects.filter(user=request.user, product_size_color=product_size_color).first()

        if not cart:
            if count > product_size_color.count:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
            Cart.objects.create(user=request.user, product_size_color=product_size_color, quantity=count)
            messages.success(request, 'This product is successfully added to the cart!')
        else:
            if cart.quantity + count > product_size_color.count:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
            cart.quantity += count
            cart.save()
        messages.success(request, 'This product is successfully added to the cart!')

    except Exception as e:
        messages.error(request, 'Error occurred.')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def update_product_count_in_cart(request):
    data = json.loads(request.body.decode('utf-8'))
    count = int(data.get('count'))
    product = int(data.get('product'))

    cart = Cart.objects.get(user=request.user, product_size_color=product)

    if not cart:
        Cart.objects.create(user=request.user, product_size_color=product,
                            quantity=count)
    else:
        cart.quantity = count
        cart.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
