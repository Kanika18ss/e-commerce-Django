# Generated by Django 5.0.6 on 2024-06-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_delete_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='delivery_status',
            field=models.CharField(max_length=100),
        ),
    ]
