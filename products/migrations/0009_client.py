# Generated by Django 3.2.10 on 2022-01-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220103_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
