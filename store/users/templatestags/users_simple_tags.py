from django import template

import products.methods
from products.models import Product, ProductImage

register = template.Library()


@register.simple_tag()
def get_review_count(product):
    pass
