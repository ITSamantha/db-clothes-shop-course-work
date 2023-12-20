from django.core.mail import send_mail
from django.http import HttpResponse, BadHeaderError

from orders.models import Cart


def get_cart_products(user):
    cart = Cart.objects.filter(user=user)
    return cart


def reduce_products(user):
    carts = Cart.objects.filter(user=user)
    for item in carts:
        product = item.product_size_color
        product.count -= item.quantity
        if product.count == 0:
            product.delete()
        else:
            product.save()
    carts.delete()
