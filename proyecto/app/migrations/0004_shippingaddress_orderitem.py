# Generated by Django 5.1.4 on 2024-12-29 23:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_address_shippingaddress_ciudad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='orderitem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.orderitem'),
        ),
    ]