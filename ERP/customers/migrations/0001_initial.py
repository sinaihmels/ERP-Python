# Generated by Django 5.0.3 on 2024-04-07 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=400)),
                ('phone', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id_comma_amount_comma_price_semicolon', models.TextField(max_length=400)),
                ('notes', models.TextField(max_length=400)),
                ('delivery_address', models.CharField(max_length=400)),
                ('delivery_name', models.CharField(max_length=200)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('status', models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.SET, to='customers.status')),
            ],
        ),
    ]
