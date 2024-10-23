# Generated by Django 5.1.1 on 2024-10-11 13:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_alter_station_x_coordinate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.station')),
            ],
            options={
                'verbose_name_plural': 'Station Logs',
                'ordering': ['-timestamp'],
            },
        ),
    ]
