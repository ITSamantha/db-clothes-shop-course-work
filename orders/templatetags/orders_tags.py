from django import template

import dictionaries.cart_table
from orders.models import Cart, Favourites

register = template.Library()


@register.simple_tag()
def get_cart_count_products(user):
    count = Cart.objects.filter(user=user).count()
    return count


@register.simple_tag()
def get_favourite_count_products(user):
    count = Favourites.objects.filter(user=user).count()
    return count


@register.simple_tag()
def get_cart_table_header():
    return dictionaries.cart_table.CART_TABLE
