from django import template

import products.utils
from products.models import Product, ProductImage

register = template.Library()

