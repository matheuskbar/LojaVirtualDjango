# Generated by Django 3.2.8 on 2021-11-05 12:48

from django.db import migrations
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_cep'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='postal_code',
            field=localflavor.br.models.BRPostalCodeField(default=1, max_length=9, verbose_name='CEP'),
            preserve_default=False,
        ),
    ]