# Generated by Django 3.2.10 on 2022-01-31 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_quiqorder_quiqorderline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiqorder',
            name='remaining_atthattime',
        ),
    ]
