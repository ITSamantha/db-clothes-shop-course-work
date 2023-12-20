from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from products.models import Product
from users.models import User


class Country(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.name}'


class CountryCity(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('country', 'city')
        verbose_name = 'Country & City'
        verbose_name_plural = 'Countries & Cities'

    def __str__(self):
        return f'{self.country}, {self.city}'


class Demand(models.Model):
    name = models.CharField(max_length=64, verbose_name='Name')
    email = models.EmailField(max_length=128, verbose_name='Email')
    subject = models.CharField(max_length=64, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    created = models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Creation Date')

    class Meta:
        verbose_name = 'Demand'
        verbose_name_plural = 'Demands'
        unique_together = ('name', 'email', 'subject', 'message')

    def __str__(self):
        return f"{self.name} | {self.subject}"
