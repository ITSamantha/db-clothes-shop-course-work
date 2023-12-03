from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class City(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class CountryCity(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)  # TODO: CHANGE
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)  # TODO: CHANGE

    class Meta:
        unique_together = ('country_id', 'city_id')
        verbose_name = 'Country & City'
        verbose_name_plural = 'Countries & Cities'
