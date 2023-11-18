# Generated by Django 3.2 on 2023-11-18 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_categorysex_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='category_sex_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='products.categorysex'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='productcategory',
            unique_together={('product_id', 'category_sex_id')},
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='category_id',
        ),
    ]
