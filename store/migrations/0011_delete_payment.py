# Generated by Django 5.0.6 on 2024-06-27 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_orderitem_delivery_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]