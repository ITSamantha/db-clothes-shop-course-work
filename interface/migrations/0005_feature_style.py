# Generated by Django 4.2.8 on 2023-12-20 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0004_alter_feature_name_alter_vendor_image_network'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='style',
            field=models.CharField(default='fa fa-check', max_length=64, verbose_name='Feature Style'),
        ),
    ]