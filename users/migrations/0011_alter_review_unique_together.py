# Generated by Django 4.2.8 on 2023-12-20 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_alter_product_date_create'),
        ('users', '0010_rename_product_id_review_product_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'product')},
        ),
    ]