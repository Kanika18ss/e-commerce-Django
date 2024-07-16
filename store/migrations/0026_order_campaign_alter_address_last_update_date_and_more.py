# Generated by Django 5.0.6 on 2024-06-27 17:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_alter_orderitem_billing_address_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='campaign',
            field=models.ForeignKey(default='home', on_delete=django.db.models.deletion.CASCADE, to='store.campaign'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='last_update_date',
            field=models.DateTimeField(auto_now_add=True),
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