# Generated by Django 5.0.7 on 2024-07-24 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_products_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.categories', verbose_name='Категория'),
        ),
    ]
