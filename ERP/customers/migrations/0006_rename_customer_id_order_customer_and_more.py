# Generated by Django 5.0.3 on 2024-04-09 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
    ]
