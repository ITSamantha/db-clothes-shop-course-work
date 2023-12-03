from django.contrib import admin
from products.models import *
from inlines import *

LIST_PER_PAGE = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    ordering = ['id']
    list_per_page = LIST_PER_PAGE
    search_fields = ['name', 'id']
    show_full_result_count = True


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    ordering = ['id']
    list_per_page = LIST_PER_PAGE
    search_fields = ['name', 'id']
    show_full_result_count = True


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    ordering = ['id']
    list_per_page = LIST_PER_PAGE
    search_fields = ['name', 'id']
    show_full_result_count = True


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    ordering = ['id']
    list_per_page = LIST_PER_PAGE
    search_fields = ['name', 'id']
    show_full_result_count = True


"""
@admin.register(ProductCategoryGender)
class ProductCategoryGenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'gender')
    list_display_links = ('id', 'category', 'gender')
    ordering = ['id']
    list_filter = ('category', 'gender')
"""





@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name', 'category_gender__category__name', 'category_gender__gender__name')
    # list_filter = ('category_gender__category', 'category_gender__gender')

    inlines = [
        ProductSizeColorInline,
        ProductCategoryGenderInline,
        ProductImageInline,
    ]

    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'price', 'short_description', 'long_description', 'additional_information')
        }),
    )
