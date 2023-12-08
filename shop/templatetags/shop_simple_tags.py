from django import template

from dictionaries import topics, networks, pages, features, vendors, shop_info

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


@register.simple_tag()
def get_vendors():
    return vendors.VENDORS


@register.simple_tag()
def get_shop_info():
    return shop_info.SHOP_INFO
