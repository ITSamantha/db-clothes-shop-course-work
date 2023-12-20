from django import template

import products.utils
from products.models import *

register = template.Library()


@register.simple_tag()
def max_product_price():
    maximum = products.utils.get_max_product_price()
    return maximum


@register.simple_tag()
def min_product_price():
    minimum = products.utils.get_min_product_price()
    return minimum


@register.simple_tag()
def get_product_images(product_id, limit=None):
    images = ProductImage.objects.filter(product__id=product_id) if limit is None else ProductImage.objects.filter(
        product__id=product_id)[:limit]
    return images


@register.simple_tag()
def get_product_size_color_count_info(product):
    info = products.utils.get_product_size_color_count_info(product)
    return info


@register.simple_tag()
def get_product_sizes(product):
    sizes = products.utils.get_product_sizes(product)
    return sizes


@register.simple_tag()
def get_product_colors(product):
    colors = products.utils.get_product_colors(product)
    return colors


@register.simple_tag()
def get_categories():
    categories = Category.objects.filter(productcategorygender__product__isnull=False).distinct()
    return categories


@register.simple_tag()
def get_categories_counts():
    categories = products.utils.get_categories_counts()
    return categories


@register.simple_tag()
def get_product_reviews(product):
    reviews = products.utils.get_product_reviews(product)
    return reviews
