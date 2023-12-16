from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

import products.utils
from products import utils
from products.models import *


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['product_id']
        context['product_images'] = utils.get_product_images(product_id)
        return context


def get_size_details(request, product_id):
    sizes = ProductSizeColor.objects.filter(product=product_id).values('size__id', 'size__name')
    if 'size' in request.GET:
        size = int(request.GET['size'])
    else:
        size = ProductSizeColor.objects.filter(product=product_id).first().size.id
    colors = ProductSizeColor.objects.filter(size=size)
    context = {
        'size': size,
        'colors': colors,
        'sizes': sizes,
    }
    return render(request, 'products/includes/product_detail_colors_sizes.html', context=context)


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


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = utils.get_categories()
        context['just_arrived_products'] = utils.get_just_arrived_limited()
        context['trendy_products'] = utils.get_trendy_products_limited()
        return context


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
