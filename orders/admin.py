from django.contrib import admin
from orders.models import *
from shop.admin import BaseAdminModel


@admin.register(Status)
class StatusAdmin(BaseAdminModel):
    pass


@admin.register(PaymentType)
class PaymentTypeAdmin(BaseAdminModel):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'user', 'product_size_color', 'quantity')
    search_fields = ('user', 'product_size_color')
    ordering = ['id']
    list_per_page = 10
    show_full_result_count = True


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
