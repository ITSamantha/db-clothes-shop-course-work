from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Subquery, Count, OuterRef, F, Prefetch

from products.models import *

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
    categories_counts = ProductCategoryGender.objects.values(name=F('category_gender__category__name'),
                                                             column_id=F('category_gender__category__id')).annotate(
        Count("product", distinct=True))
    return categories_counts


def get_all_products():
    products = Product.objects.all()
    return products
