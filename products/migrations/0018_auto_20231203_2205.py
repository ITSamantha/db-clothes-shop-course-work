# Generated by Django 3.2 on 2023-12-03 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20231203_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategoryGender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='category')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.gender', verbose_name='gender')),
            ],
            options={
                'verbose_name': 'Category & Gender',
                'verbose_name_plural': 'Categories & Genders',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_gender',
        ),
        migrations.DeleteModel(
            name='CategoryGender',
        ),
        migrations.AddField(
            model_name='productcategorygender',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product'),
        ),
        migrations.AlterUniqueTogether(
            name='productcategorygender',
            unique_together={('category', 'gender')},
        ),
    ]
