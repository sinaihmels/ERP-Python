# Generated by Django 5.0.3 on 2024-04-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.BigIntegerField(default=0),
        ),
    ]
