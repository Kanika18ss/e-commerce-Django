# Generated by Django 5.0.6 on 2024-06-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_orderitem_billing_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='cancellation_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='delivery_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]