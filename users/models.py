from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images/', null=True, blank=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    mobile_phone = models.CharField(max_length=11)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Review(models.Model):
    rating = models.FloatField(validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.date} | {self.user_id} | {self.product_id}"

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Subscribe(models.Model):
    name = models.CharField(max_length=128, verbose_name='User Name')
    email = models.CharField(max_length=128, verbose_name='User Email')

    class Meta:
        unique_together = ('name', 'email')
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'
