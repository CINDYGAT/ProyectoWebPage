# Generated by Django 5.1.4 on 2024-12-28 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address',
            new_name='ciudad',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='city',
            new_name='departamento',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='state',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='zipcode',
            new_name='pais',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='zip',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
