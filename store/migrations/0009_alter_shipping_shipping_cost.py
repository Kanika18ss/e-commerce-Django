# Generated by Django 5.0.6 on 2024-06-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_orderitem_billing_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='shipping_cost',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
