# Generated by Django 3.2.10 on 2022-02-07 08:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_incomingorder_empty_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingorder',
            name='paid',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='تم دفع'),
        ),
        migrations.AlterField(
            model_name='incomingorder',
            name='remaining_money',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='رصيد ما قبله'),
        ),
        migrations.AlterField(
            model_name='incomingorder',
            name='seller',
            field=models.CharField(max_length=100, null=True, verbose_name='التاجر'),
        ),
        migrations.AlterField(
            model_name='incomingorder',
            name='still',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='مازال'),
        ),
        migrations.AlterField(
            model_name='incomingorder',
            name='total',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='سعر الفاتوره'),
        ),
        migrations.AlterField(
            model_name='incomingorder',
            name='total2',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='الاجمالى'),
        ),
    ]
