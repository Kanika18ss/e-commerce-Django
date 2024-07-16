# Generated by Django 5.0.6 on 2024-06-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_alter_address_last_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='campaign_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_keywords',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_title',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='COD', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_method',
            field=models.CharField(default='standard', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='delivery_status',
            field=models.CharField(default='pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='payment_method',
            field=models.CharField(default='COD', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='shipping_method',
            field=models.CharField(default='standard', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_title',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='original_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='small_description',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(default='', max_length=150),
        ),
    ]
