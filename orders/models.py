from django.db import models

from products.models import ProductSizeColor
from users.models import User


class Status(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class PaymentType(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Payment Type'
        verbose_name_plural = 'Payment Types'


class Cart(models.Model):
    quantity = models.PositiveIntegerField(verbose_name='Product Quantity')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Creation Date')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='User')
    product_size_color = models.ForeignKey(ProductSizeColor, on_delete=models.PROTECT, verbose_name='Product')

    def __str__(self):
        return f"{self.product_size_color}| {self.user}"

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        unique_together = ('user', 'product_size_color')
