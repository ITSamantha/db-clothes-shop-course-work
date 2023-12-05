from django.contrib import admin
from orders.models import *
from shop.admin import BaseAdminModel


@admin.register(Status)
class StatusAdmin(BaseAdminModel):
    pass


@admin.register(PaymentType)
class PaymentTypeAdmin(BaseAdminModel):
    pass
