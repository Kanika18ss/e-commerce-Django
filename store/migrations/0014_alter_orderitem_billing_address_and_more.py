# Generated by Django 5.0.6 on 2024-06-27 16:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_orderitem_delivery_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='billing_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='billing_order_items', to='store.address'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='cancellation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
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
