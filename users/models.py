from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from products.models import Product


class User(AbstractUser):
    class Sex(models.TextChoices):
        FEMALE = 'F', 'Female'
        MALE = 'M', 'MALE'

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed.")

    image = models.ImageField(upload_to='users_images/', default='users_images/default.png')
    sex = models.CharField(max_length=1, choices=Sex.choices, default=Sex.FEMALE)
    birthday = models.DateField(blank=True, null=True)
    mobile_phone = models.CharField(validators=[phone_regex], max_length=12, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Subscribe(models.Model):
    name = models.CharField(max_length=128, verbose_name='User Name')
    email = models.CharField(max_length=128, verbose_name='User Email', unique=True)

    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'

    def __str__(self):
        return self.email


class Review(models.Model):
    rating = models.FloatField(validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, auto_created=True)

    def __str__(self):
        return f"{self.date} | {self.user_id} | {self.product_id}"

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
