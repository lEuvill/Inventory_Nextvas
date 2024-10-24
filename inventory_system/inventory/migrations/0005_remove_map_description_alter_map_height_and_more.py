# Generated by Django 5.1.1 on 2024-10-08 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_remove_map_inventory_item_remove_map_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='description',
        ),
        migrations.AlterField(
            model_name='map',
            name='height',
            field=models.PositiveIntegerField(default=600),
        ),
        migrations.AlterField(
            model_name='map',
            name='width',
            field=models.PositiveIntegerField(default=800),
        ),
        migrations.AlterField(
            model_name='station',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.map'),
        ),
    ]
