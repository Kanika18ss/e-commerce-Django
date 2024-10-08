# Generated by Django 5.0.6 on 2024-06-28 05:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0035_payment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('shipping_id', models.AutoField(primary_key=True, serialize=False)),
                ('shipping_date', models.DateTimeField()),
                ('estimated_delivery_date', models.DateTimeField()),
                ('actual_delivery_date', models.DateTimeField(blank=True, null=True)),
                ('carrier_name', models.CharField(max_length=255)),
                ('tracking_number', models.CharField(max_length=255)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_method', models.CharField(max_length=255)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.order')),
                ('shipping_address_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.address')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
