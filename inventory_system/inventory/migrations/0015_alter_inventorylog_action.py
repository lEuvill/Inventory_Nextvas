# Generated by Django 5.1.1 on 2024-10-09 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_alter_inventorylog_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorylog',
            name='action',
            field=models.CharField(max_length=100),
        ),
    ]
