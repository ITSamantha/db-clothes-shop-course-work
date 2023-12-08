from django.contrib import admin
from interface.models import *


# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_filter = ('name',)
    list_per_page = 10
    list_display_links = ('id',)
    search_fields = ('name', 'url')

    fieldsets = (
        ('Partner Information', {
            'fields': (
                'name', 'image', 'url')
        }),
    )
