from django import template

from orders.models import Cart

register = template.Library()


@register.simple_tag()
def get_cart_count_products(user):
    count = Cart.objects.filter(user=user).count()
    return count


@register.simple_tag()
def get_favourite_count_products(user):
    count = Favourite.objects.filter(user=user).count()
    return count
