from core.admin import BaseAdminModel, LIST_PER_PAGE
from shop.inlines import *


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


@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    pass
