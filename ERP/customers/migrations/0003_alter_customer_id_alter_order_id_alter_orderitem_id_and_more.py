# Generated by Django 5.0.3 on 2024-04-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_remove_order_delivery_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
