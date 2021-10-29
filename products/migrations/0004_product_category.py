# Generated by Django 3.2.8 on 2021-10-26 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=3, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.category'),
            preserve_default=False,
        ),
    ]
