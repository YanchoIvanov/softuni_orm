# Generated by Django 4.2.7 on 2023-11-12 08:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18, 'Age must be greater than 18')]),
        ),
    ]
