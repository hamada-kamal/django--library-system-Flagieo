# Generated by Django 3.2.10 on 2022-01-29 12:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220129_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='skype_session_attendance',
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='تم دفع'),
        ),
    ]