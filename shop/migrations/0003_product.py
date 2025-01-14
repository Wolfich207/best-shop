# Generated by Django 4.1.7 on 2023-03-27 14:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_options_alter_category_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('description', models.CharField(blank=True, max_length=700, verbose_name='описание')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='', verbose_name='изображение')),
                ('url', models.SlugField(unique=True, verbose_name='URL')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0, 'цена должна быть не меньше 0')], verbose_name='цена')),
                ('category_for_products', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='категория')),
            ],
        ),
    ]
