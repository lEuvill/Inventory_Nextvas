# Generated by Django 5.1.1 on 2024-10-11 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_inventorylog_item_model_inventorylog_serial_number_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventorylog',
            options={'verbose_name_plural': '(ADMIN) Inventory Logs'},
        ),
    ]