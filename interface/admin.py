from django.contrib import admin
from interface.models import *


# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_per_page = 10
    list_display_links = ('id',)
    search_fields = ('name', 'url')

    fieldsets = (
        ('Partner Information', {
            'fields': (
                'name', 'image', 'url')
        }),
    )


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_editable = ('name',)
    search_fields = ('name', 'id')
    list_per_page = 10


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'style')
    list_display_links = ('id',)
    search_fields = ('id', 'name', 'url', 'style')
