# Generated by Django 4.2.8 on 2023-12-16 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
