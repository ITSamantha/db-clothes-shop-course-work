from django.http import HttpResponse
from django.shortcuts import render

import products.utils
from dictionaries.features import *
from products import utils
from products.models import *


def product_details(request, product_id):
    product_object = Product.objects.get(id=product_id)

    context = {
        'product': product_object,
    }

    return render(request, 'products/detail.html', context=context)


def product_category(request, category):
    return render(request, 'products/category.html')


def shop(request):
    colors_counts = utils.get_colors_counts()
    sizes_counts = utils.get_sizes_counts()
    categories_counts = utils.get_categories_counts()
    products = utils.get_all_products()

    context = {
        'colors_counts': colors_counts,
        'sizes_counts': sizes_counts,
        'categories_counts': categories_counts,
        'products': products,
    }

    return render(request, 'products/shop.html', context=context)


def index(request):
    categories = utils.get_categories()
    just_arrived_products = utils.get_just_arrived_limited()
    trendy_products = utils.get_trendy_products_limited()
    context = {
        'categories': categories,
        'just_arrived_products': just_arrived_products,
        'trendy_products': trendy_products,
    }

    return render(request, 'products/index.html', context=context)


def filter_products(request):
    if request.method == 'GET':
        colors = request.GET.get('colors')
        categories = request.GET.get('categories')
        sizes = request.GET.get('sizes')

        prods = products.utils.filter_products(colors, categories, sizes)
        context = {
            'products': prods,
        }

        return render(request, 'products/includes/shop_products.html', context=context)
    return HttpResponse('Page not found')
