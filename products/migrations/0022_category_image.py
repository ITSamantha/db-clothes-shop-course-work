# Generated by Django 4.2.8 on 2023-12-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_productsizecolor_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='img/categories_images/default.jpeg', upload_to='categories_images/'),
        ),
    ]
