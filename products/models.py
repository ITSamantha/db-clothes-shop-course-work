from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Gender(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name}"


class Size(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name}"


class Color(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.name}"


class CategoryGender(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('category', 'gender')

    def __str__(self):
        return f"{self.category}| {self.gender}"


class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    price = models.FloatField(validators=[MinValueValidator(0)], default=None)
    short_description = models.CharField(max_length=256, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"ID: {self.id}| Название: {self.name}"


class ProductSizeColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}| Размер:{self.size}| Цвет: {self.color}"

    class Meta:
        unique_together = ('product', 'size', 'color')


class ProductSizeColorCount(models.Model):
    product_size_color = models.ForeignKey(ProductSizeColor, on_delete=models.CASCADE, unique=True)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product_size_color}| Количество: {self.count}"


class ProductImage(models.Model):
    image = models.ImageField(upload_to='static/img/product_images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} | {self.image}"


class ProductCategoryGender(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_gender = models.ForeignKey(CategoryGender, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}| {self.category_gender}"

    class Meta:
        unique_together = ('product', 'category_gender')
