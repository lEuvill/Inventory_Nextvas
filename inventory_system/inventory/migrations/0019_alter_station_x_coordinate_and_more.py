# Generated by Django 5.1.1 on 2024-10-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_rename_equipment_station_items_remove_station_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='x_coordinate',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='station',
            name='y_coordinate',
            field=models.PositiveIntegerField(),
        ),
    ]
