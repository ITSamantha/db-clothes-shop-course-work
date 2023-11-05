from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=64, unique=True)


class City(models.Model):
    name = models.CharField(max_length=64, unique=True)


class CountryCity(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)  # TODO: CHANGE
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)  # TODO: CHANGE

    class Meta:
        unique_together = ('country_id', 'city_id')


class Status(models.Model):
    name = models.CharField(max_length=64, unique=True)


class PaymentType(models.Model):
    name = models.CharField(max_length=64, unique=True)
