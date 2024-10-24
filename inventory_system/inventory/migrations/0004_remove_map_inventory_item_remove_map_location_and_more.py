# Generated by Django 5.1.1 on 2024-10-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_station'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='inventory_item',
        ),
        migrations.RemoveField(
            model_name='map',
            name='location',
        ),
        migrations.AddField(
            model_name='map',
            name='height',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='map',
            name='width',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='station',
            name='x_coordinate',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='station',
            name='y_coordinate',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
