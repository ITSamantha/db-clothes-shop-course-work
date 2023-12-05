from django.core.validators import MinValueValidator
from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='gender')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'


class Size(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='size')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'


class Color(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='color')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='category')
    image = models.ImageField(upload_to='categories_images/', default='categories_images/default.jpeg',
                              verbose_name='image')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name='product name')
    price = models.FloatField(validators=[MinValueValidator(0)], default=None, verbose_name='price')
    short_description = models.CharField(max_length=256, blank=True, null=True, verbose_name='short description')
    long_description = models.TextField(blank=True, null=True, verbose_name='long description')
    additional_information = models.TextField(blank=True, null=True, verbose_name='additional information')

    def __str__(self):
        return f"{self.id} | {self.name}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product', related_name='images')
    image = models.ImageField(upload_to='product_images/', verbose_name='image', default='img/default-product.png')

    def __str__(self):
        return f"{self.product} | {self.image}"

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class ProductCategoryGender(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, verbose_name='gender')

    class Meta:
        unique_together = ('category', 'gender', 'product')
        verbose_name = 'Category & Gender'
        verbose_name_plural = 'Categories & Genders'

    def __str__(self):
        return f"{self.category} | {self.gender}"


class ProductSizeColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name='size', related_name='size')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='color')
    count = models.PositiveIntegerField(verbose_name='count of product')

    def __str__(self):
        return f"{self.size} | {self.color}"

    class Meta:
        unique_together = ('size', 'color', 'product')
        verbose_name = 'Size & Color'
        verbose_name_plural = 'Sizes & Colors'
