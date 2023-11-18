from django.shortcuts import render

from dictionaries import networks, topics
from dictionaries.features import *
from products.models import *


def product_details(request):
    return render(request, 'products/detail.html')


def product_category(request, category):
    return render(request, 'products/category.html')


def shop(request):
    return render(request, 'products/shop.html')


def index(request):
    categories = Category.objects.all()

    context = {
        'features': FEATURES,
        'general_categories': CATEGORIES_GENERAL,
        'sales': SALES,
        'vendors': VENDORS,
        'topics': topics.TOPICS,
        'networks': networks.NETWORKS,
        'categories': categories,
    }
    return render(request, 'products/index.html', context=context)
