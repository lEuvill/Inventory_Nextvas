# Generated by Django 5.1.1 on 2024-10-08 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_map'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('equipment', models.ManyToManyField(blank=True, to='inventory.inventoryitem')),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='inventory.map')),
            ],
        ),
    ]