# Generated by Django 5.1.1 on 2024-10-09 17:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_alter_inventorylog_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorylog',
            name='item_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventorylog',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.inventoryitem'),
        ),
    ]
