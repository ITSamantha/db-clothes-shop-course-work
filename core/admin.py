from django.contrib import admin

LIST_PER_PAGE = 10


class BaseAdminModel(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    ordering = ['id']
    list_per_page = LIST_PER_PAGE
    search_fields = ['name', 'id']
    show_full_result_count = True
