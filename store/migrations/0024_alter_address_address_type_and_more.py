# Generated by Django 5.0.6 on 2024-06-27 17:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_alter_address_address_type_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='apartment_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='building_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='contact_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='delivery_instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='floor_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='gate_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='billing_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='billing_order_items', to='store.address'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.product'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='shipping_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='shipping_order_items', to='store.address'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]