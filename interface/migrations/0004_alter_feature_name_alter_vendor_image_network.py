# Generated by Django 4.2.8 on 2023-12-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Feature'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(upload_to='vendor_images/', verbose_name='Partner Logo Image'),
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Network')),
                ('style', models.CharField(blank=True, max_length=128, null=True, verbose_name='Network Style')),
                ('url', models.CharField(blank=True, max_length=512, null=True, verbose_name='Website')),
            ],
            options={
                'verbose_name': 'Network',
                'verbose_name_plural': 'Networks',
                'unique_together': {('name', 'url')},
            },
        ),
    ]