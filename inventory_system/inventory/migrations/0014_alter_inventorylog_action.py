# Generated by Django 5.1.1 on 2024-10-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_remove_inventorylog_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorylog',
            name='action',
            field=models.CharField(max_length=255),
        ),
    ]
