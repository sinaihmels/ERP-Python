# Generated by Django 5.0.3 on 2024-03-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_productclass_color_item_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='amount_instock',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]
