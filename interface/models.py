from django.db import models


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Partner Name')
    image = models.ImageField(upload_to='vendor_images/', verbose_name='Partner Logo Image')
    url = models.CharField(max_length=512, blank=True, null=True, verbose_name='Partner Website')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
        unique_together = ('name', 'url')


class Feature(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Feature')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'


class Network(models.Model):
    name = models.CharField(max_length=64, verbose_name='Network')
    style = models.CharField(max_length=128, blank=True, null=True, verbose_name='Network Style')
    url = models.CharField(max_length=512, blank=True, null=True, verbose_name='Website')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Network'
        verbose_name_plural = 'Networks'
        unique_together = ('name', 'url')
