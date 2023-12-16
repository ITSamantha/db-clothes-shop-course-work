from django import template

import interface.utils
from dictionaries import topics, pages, shop_info

register = template.Library()


@register.simple_tag()
def get_topics():
    return topics.TOPICS


@register.simple_tag()
def get_networks():
    networks = interface.utils.get_networks()
    return networks


@register.simple_tag()
def get_pages():
    return pages.PAGES


@register.simple_tag()
def get_features():
    features = interface.utils.get_features()
    return features


@register.simple_tag()
def get_vendors():
    vendors = interface.utils.get_vendors()
    return vendors


@register.simple_tag()
def get_shop_info():
    return shop_info.SHOP_INFO
