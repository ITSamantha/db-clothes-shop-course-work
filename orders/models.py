from django.db import models


# Create your models here.

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
