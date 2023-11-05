from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Size(models.Model):
    name = models.CharField(max_length=10, unique=True)


class Color(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    price = models.FloatField(validators=[MinValueValidator(0)], default=None)
    short_description = models.CharField(max_length=256, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)


class ProductSizeColor(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_id = models.ForeignKey(Size, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product_id', 'size_id', 'color_id')


class ProductSizeColorCount(models.Model):
    product_size_color_id = models.ForeignKey(ProductSizeColor, on_delete=models.CASCADE, unique=True)
    count = models.PositiveIntegerField()


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/product_images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    default = models.BooleanField(default=False)


class ProductCategory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product_id', 'category_id')
