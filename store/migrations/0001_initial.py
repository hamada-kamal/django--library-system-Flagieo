# Generated by Django 3.2.10 on 2022-01-10 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='رقم الهاتف')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='اسم العميل')),
                ('remaining_money', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='مبلغ متبقى')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56, unique=True, verbose_name='اسم المنتج')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='السعر')),
                ('wholesale_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='سعر الجملة')),
                ('available_in_ventory', models.PositiveIntegerField(verbose_name='متوفر')),
                ('discription', models.TextField(blank=True, max_length=200, null=True, verbose_name='الوصف')),
                ('count_sold', models.IntegerField(default=0, verbose_name='تم بيع')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الانشاء')),
                ('code', models.CharField(max_length=100, null=True)),
                ('PROslug', models.SlugField(allow_unicode=True, blank=True, max_length=255, null=True, unique=True, verbose_name='slug')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('end_bill', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('ORDslug', models.SlugField(allow_unicode=True, blank=True, max_length=255, null=True, unique=True, verbose_name='slug')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.client', verbose_name='العميل')),
            ],
        ),
    ]