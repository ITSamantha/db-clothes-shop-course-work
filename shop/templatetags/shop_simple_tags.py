from django.db.models import Max, Min
from django import template

from dictionaries import topics, networks, pages, features

# from products.models import Product, ProductImage

register = template.Library()


@register.simple_tag()
def get_topics():
    return topics.TOPICS


@register.simple_tag()
def get_networks():
    return networks.NETWORKS


@register.simple_tag()
def get_pages():
    return pages.PAGES


@register.simple_tag()
def get_features():
    return features.FEATURES
