from django.shortcuts import render

import dictionaries.topics
import dictionaries.networks
from dictionaries.features import FEATURES
from products.models import Category


# Create your views here.

def cart(request):
    categories = Category.objects.all()
    context = {
        'features': FEATURES,
        'topics': dictionaries.topics.TOPICS,
        'networks': dictionaries.networks.NETWORKS,
        'categories': categories,
    }
    return render(request, 'orders/cart.html', context=context)


def checkout(request):
    categories = Category.objects.all()
    context = {
        'features': FEATURES,
        'topics': dictionaries.topics.TOPICS,
        'networks': dictionaries.networks.NETWORKS,
        'categories': categories,
    }
    return render(request, 'orders/checkout.html', context=context)


def favourites(request):
    categories = Category.objects.all()
    context = {
        'features': FEATURES,
        'topics': dictionaries.topics.TOPICS,
        'networks': dictionaries.networks.NETWORKS,
        'categories': categories,
    }
    return render(request, 'orders/favourites.html', context=context)
