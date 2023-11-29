from django import template

import products.methods
from products.models import Product, ProductImage

register = template.Library()


@register.simple_tag()
def max_product_price():
    maximum = products.methods.get_max_product_price()
    return maximum


@register.simple_tag()
def min_product_price():
    minimum = products.methods.get_min_product_price()
    return minimum


@register.simple_tag()
def get_product_images(product_id):
    images = ProductImage.objects.filter(product__id=product_id, default=False)
    return images


@register.simple_tag()
def get_product_size_color_count_info(product):
    info = products.methods.get_product_size_color_count_info(product)
    return info


@register.simple_tag()
def get_product_sizes(product):
    sizes = products.methods.get_product_sizes(product)
    return sizes


@register.simple_tag()
def get_product_colors(product):
    colors = products.methods.get_product_colors(product)
    return colors
