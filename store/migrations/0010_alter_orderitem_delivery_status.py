# Generated by Django 5.0.6 on 2024-06-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_shipping_shipping_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='delivery_status',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]
