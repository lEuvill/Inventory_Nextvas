# Generated by Django 5.1.1 on 2024-10-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_inventorylog_item_name_alter_inventorylog_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorylog',
            name='action',
            field=models.CharField(max_length=255),
        ),
    ]