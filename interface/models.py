from django.db import models


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Partner Name')
    image = models.ImageField(upload_to='vendors/', verbose_name='Partner Logo Image', default='img')
    url = models.CharField(max_length=512, blank=True, null=True, verbose_name='Partner Website')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
        unique_together = ('name', 'url')
