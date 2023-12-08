# Generated by Django 4.2.8 on 2023-12-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_image'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscribe',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.CharField(max_length=128, unique=True, verbose_name='User Email'),
        ),
    ]
