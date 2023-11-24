from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Subquery, Count, OuterRef, F, Prefetch

from products.models import *

TARGET_COLUMN = 'column_name'


def get_colors_counts():
    colors_counts = ProductSizeColor.objects.values(name=F(f'color__name')).annotate(
        Count("product", distinct=True))
    return colors_counts


def get_sizes_counts():
    sizes_counts = ProductSizeColor.objects.values(name=F('size__name')).annotate(Count("product", distinct=True))
    return sizes_counts


def get_categories_counts():
    categories_counts = ProductCategoryGender.objects.values(name=F('category_gender__category__name')).annotate(
        Count("product", distinct=True))
    return categories_counts


def get_all_products():
    products = Product.objects.all()
    print(products)
    return products
