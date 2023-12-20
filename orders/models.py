import json

from django.core.serializers import serialize, deserialize
from django.core.serializers.json import DjangoJSONEncoder
from django.core.validators import RegexValidator
from django.db import models

from shop.models import CountryCity
from products.models import ProductSizeColor
from users.models import User


class Status(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class PaymentType(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Payment Type'
        verbose_name_plural = 'Payment Types'


class BaseProductList(models.Model):
    created_at = models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Creation Date')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    product_size_color = models.ForeignKey(ProductSizeColor, on_delete=models.CASCADE, verbose_name='Product')

    def __str__(self):
        return f"{self.product_size_color}| {self.user}"

    class Meta:
        unique_together = ('user', 'product_size_color')


class Cart(BaseProductList):
    quantity = models.PositiveIntegerField(verbose_name='Product Quantity')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def sum(self):
        return self.quantity * self.product_size_color.product.price

    def serialize(self):
        data = {
            'id': self.id,
            'quantity': self.quantity,
            'created_at': self.created_at,
            'product_size_color_id': self.product_size_color.id,
        }
        return data

    @classmethod
    def serialize_cart(cls, user):
        cart_data = [cart.serialize() for cart in Cart.objects.filter(user=user)]
        return cart_data


class Favourites(BaseProductList):
    class Meta:
        verbose_name = 'Favourite'
        verbose_name_plural = 'Favourites'


class Order(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed.")

    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Customer')
    first_name = models.CharField(max_length=128, verbose_name='First Name')
    last_name = models.CharField(max_length=128, verbose_name='Last Name')
    email = models.EmailField(max_length=128, verbose_name='Email')
    mobile_phone = models.CharField(validators=[phone_regex], max_length=12, verbose_name='Mobile Phone')
    address = models.CharField(max_length=256, verbose_name='Address')
    country_city = models.ForeignKey(CountryCity, on_delete=models.PROTECT, verbose_name='Country & City')
    postal_code = models.CharField(max_length=6, verbose_name='Postal Code')
    created = models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Created At')
    updated = models.DateTimeField(auto_now=True, auto_created=True, verbose_name='Last Updated')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Order Status')
    cart = models.JSONField(verbose_name='Cart')
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT, verbose_name='Payment Type')

    def save(self, *args, **kwargs):
        cart_data = json.dumps(Cart.serialize_cart(self.user), cls=DjangoJSONEncoder)
        print(cart_data)
        self.cart = cart_data
        super().save(*args, **kwargs)

    def get_cart_data(self):
        cart_objects = deserialize('json', self.cart)

        cart_queryset = [Cart(**cart_object['fields']) for cart_object in cart_objects]

        return cart_queryset

    def __str__(self):
        return f"{self.user} | {self.created} | {self.status}"
