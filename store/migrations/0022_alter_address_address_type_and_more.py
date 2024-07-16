# Generated by Django 5.0.6 on 2024-06-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_orderitem_cancellation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='apartment_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='building_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='contact_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='delivery_instructions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='floor_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='gate_code',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='latitude',
            field=models.DecimalField(decimal_places=8, max_digits=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='longitude',
            field=models.DecimalField(decimal_places=8, max_digits=11),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]