# Generated by Django 3.2.10 on 2022-01-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]
