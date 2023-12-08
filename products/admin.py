from products.inlines import *
from core.admin import BaseAdminModel, LIST_PER_PAGE


@admin.register(Category)
class CategoryAdmin(BaseAdminModel):
    pass


@admin.register(Gender)
class GenderAdmin(BaseAdminModel):
    pass


@admin.register(Size)
class SizeAdmin(BaseAdminModel):
    pass


@admin.register(Color)
class ColorAdmin(BaseAdminModel):
    pass


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
    list_display = \
        ('id', 'name', 'short_description', 'price', 'date_create')

    list_display_links = ('id',)
    ordering = ['id']
    list_per_page = LIST_PER_PAGE
    show_full_result_count = True
    readonly_fields = ('date_create',)

    list_filter = \
        [
            'productsizecolor__color__name',
            'productsizecolor__size__name',
            'productcategorygender__category__name',
            'productcategorygender__gender__name'
        ]

    search_fields = \
        ['name', 'short_description',
         'productsizecolor__color__name',
         'productsizecolor__size__name',
         'productcategorygender__category__name',
         'productcategorygender__gender__name',
         ]

    inlines = [
        ProductSizeColorInline,
        ProductCategoryGenderInline,
        ProductImageInline,
    ]

    fieldsets = (
        ('Product Information', {
            'fields': (
            'name', 'price', 'short_description', 'long_description', 'additional_information', 'date_create')
        }),
    )
