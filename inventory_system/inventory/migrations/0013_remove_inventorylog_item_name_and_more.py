# Generated by Django 5.1.1 on 2024-10-09 18:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_alter_inventorylog_action'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorylog',
            name='item_name',
        ),
        migrations.AlterField(
            model_name='inventorylog',
            name='action',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='inventorylog',
            name='item',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
