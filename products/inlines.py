from django.contrib import admin
from products.models import *


# Product Inlines
class ProductSizeColorInline(admin.TabularInline):
    model = ProductSizeColor
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductCategoryGenderInline(admin.TabularInline):
    model = ProductCategoryGender
    extra = 1
