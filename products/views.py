from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, TemplateView, ListView
import products.utils
from products import utils
from products.models import *
from users.forms import ReviewForm
from users.models import Review


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'

    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['product_id']
        form = ReviewForm(request.POST)
        try:
            if form.is_valid():
                cleaned_data = form.cleaned_data
                review = Review(user=request.user, product=Product.objects.get(id=product_id),
                                description=cleaned_data['description'],
                                rating=cleaned_data['rating'])
                review.save()
                messages.success(request, 'Thanks! Your review was successfully added!')
        except Exception as e:
            messages.error(request, 'Oops! An error occured! You have already written your review.')
        finally:
            return redirect('products:product_details', product_id=product_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['product_id']
        context['product_images'] = utils.get_product_images(product_id)

        product_categories = ProductCategoryGender.objects.filter(product=product_id).values('category_id').distinct()
        related_products = Product.objects.filter(productcategorygender__category__in=product_categories).exclude(
            id=product_id).distinct()
        context['products'] = related_products

        if self.request.method == 'GET':
            context['form'] = ReviewForm()

        return context


def get_size_details(request, product_id):
    sizes = ProductSizeColor.objects.filter(product__id=product_id).distinct().values('size__id', 'size__name')
    if 'size' in request.GET:
        size = int(request.GET['size'])
    else:
        size = ProductSizeColor.objects.filter(product=product_id).first().size.id
    colors = ProductSizeColor.objects.filter(size=size, product__id=product_id)
    context = {
        'size': size,
        'colors': colors,
        'sizes': sizes,
    }
    return render(request, 'products/includes/product_detail_colors_sizes.html', context=context)


def product_category(request, category):
    colors_counts = utils.get_colors_counts()
    sizes_counts = utils.get_sizes_counts()
    categories_counts = utils.get_categories_counts()
    products = utils.get_all_products()
    context = {
        'selected_category': category,
        'colors_counts': colors_counts,
        'sizes_counts': sizes_counts,
        'categories_counts': categories_counts,
        'products': products,
    }
    return render(request, 'products/shop.html', context=context)


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


class FilterProductsView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/includes/shop_products.html'

    def get_queryset(self):
        if self.request.method == 'GET':
            colors = self.request.GET.getlist('colors')
            categories = self.request.GET.getlist('categories')
            sizes = self.request.GET.getlist('sizes')
            return products.utils.filter_products(colors, categories, sizes)
        return None
