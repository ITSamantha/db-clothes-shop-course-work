from django.db.models import Max, Min, F, Count, QuerySet, Q

from products.models import *


def get_max_product_price():
    maximum = Product.objects.aggregate(Max('price'))
    return maximum['price__max']


def get_min_product_price():
    minimum = Product.objects.aggregate(Min('price'))
    return minimum['price__min']


def get_product_size_color_count(product):
    result = ProductSizeColor.objects.filter(product=product)
    return result


def get_product_sizes(product):
    sizes = ProductSizeColor.objects.filter(product=product).values('size__name', 'size__id').distinct()
    return sizes


def get_product_colors(product):
    colors = ProductSizeColor.objects.filter(product=product).values('color__name', 'color__id'
                                                                     ).distinct()
    return colors


def filter_products(colors=None, categories=None, sizes=None):
    filter_args = Q()
    if colors is not None:
        filter_args &= Q(productsizecolor__color__id__in=colors)
    if categories is not None:
        filter_args &= Q(productcategorygender__category__in=categories)
    if sizes is not None:
        filter_args &= Q(productsizecolor__size__id__in=sizes)
    products = Product.objects.filter(filter_args).distinct()
    return products


TARGET_COLUMN = 'column_name'


def get_colors_counts():
    colors_counts = ProductSizeColor.objects.values(name=F(f'color__name'), column_id=F('color__id')).annotate(
        Count("product", distinct=True))
    return colors_counts


def get_sizes_counts():
    sizes_counts = ProductSizeColor.objects.values(name=F('size__name'), column_id=F('size__id')).annotate(
        Count("product", distinct=True))
    return sizes_counts


def get_categories_counts():
    categories_counts = ProductCategoryGender.objects.values(image=F('category__image'), name=F('category__name'),
                                                             column_id=F('category__id')).annotate(
        Count("product", distinct=True))
    return categories_counts


def get_all_products():
    products = Product.objects.all()
    return products


def get_just_arrived_limited(limit=10):
    products = Product.objects.order_by('-date_create')[:limit]
    return products


def get_product_images(product_id):
    images = ProductImage.objects.filter(product__id=product_id)
    return images


def get_trendy_products_limited(limit=10):
    # TODO: RATING
    products = Product.objects.all()[:limit]
    return products


def get_categories():
    categories = Category.objects.all()
    return categories
