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
