# Generated by Django 5.0.3 on 2024-04-11 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_color_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.color'),
        ),
    ]