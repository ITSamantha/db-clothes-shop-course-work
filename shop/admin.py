from django.contrib import admin
from shop.models import *
from shop.inlines import *

LIST_PER_PAGE = 10


class BaseAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    ordering = ['id']
    list_per_page = LIST_PER_PAGE
    search_fields = ['name', 'id']
    show_full_result_count = True


@admin.register(City)
class CityAdmin(BaseAdminModel):
    pass


@admin.register(Country)
class CountryAdmin(BaseAdminModel):
    pass


@admin.register(CountryCity)
class CountryCityAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'city')
    list_display_links = ('id',)
    ordering = ['id']
    list_per_page = LIST_PER_PAGE

    search_fields = \
        ['id', 'country__name', 'city__name']

    list_filter = [
        'country',
        'city',
    ]

    show_full_result_count = True
