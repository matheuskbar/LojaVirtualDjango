# Generated by Django 3.2.8 on 2021-11-03 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20211103_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='products', to='products.Category'),
        ),
    ]
