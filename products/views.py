from django.shortcuts import render

from dictionaries import networks, topics
from dictionaries.features import *
from products import functions
from products.models import *


def product_details(request, product_id):
    print(product_id)
    product_object = Product.objects.get(id=product_id)
    context = {
        'product': product_object,
    }
    return render(request, 'products/detail.html', context=context)


def product_category(request, category):
    return render(request, 'products/category.html')


def shop(request):
    colors_counts = functions.get_colors_counts()
    sizes_counts = functions.get_sizes_counts()
    categories_counts = functions.get_categories_counts()
    products = functions.get_all_products()

    context = {
        'colors_counts': colors_counts,
        'sizes_counts': sizes_counts,
        'categories_counts': categories_counts,
        'products': products,
    }

    return render(request, 'products/shop.html', context=context)


def index(request):
    categories = Category.objects.all()

    context = {
        'features': FEATURES,
        'general_categories': CATEGORIES_GENERAL,
        'sales': SALES,
        'vendors': VENDORS,
        'categories': categories,
    }

    return render(request, 'products/index.html', context=context)
