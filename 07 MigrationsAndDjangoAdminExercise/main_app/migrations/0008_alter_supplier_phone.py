# Generated by Django 4.2.6 on 2023-10-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_supplier_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
