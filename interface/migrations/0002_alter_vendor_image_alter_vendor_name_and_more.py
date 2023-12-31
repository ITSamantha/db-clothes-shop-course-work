# Generated by Django 4.2.8 on 2023-12-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(default='img', upload_to='vendors/', verbose_name='Partner Logo Image'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Partner Name'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='url',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Partner Website'),
        ),
        migrations.AlterUniqueTogether(
            name='vendor',
            unique_together={('name', 'url')},
        ),
    ]
