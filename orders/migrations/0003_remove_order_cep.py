# Generated by Django 3.2.8 on 2021-11-05 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
    ]