from django.db.models import Max, Min
from django import template

from products.models import Product, ProductImage

register = template.Library()


@register.simple_tag()
def max_product_price():
    maximum = Product.objects.aggregate(Max('price'))
    return maximum['price__max']


@register.simple_tag()
def min_product_price():
    minimum = Product.objects.aggregate(Min('price'))
    return minimum['price__min']


@register.simple_tag()
def get_product_images(product_id):
    images = ProductImage.objects.filter(product__id=product_id, default=False)
    return images
