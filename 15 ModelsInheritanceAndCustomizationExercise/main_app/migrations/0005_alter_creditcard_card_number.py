# Generated by Django 4.2.7 on 2023-11-11 11:19

from django.db import migrations
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_creditcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='card_number',
            field=main_app.models.MaskedCreditCardField(max_length=20),
        ),
    ]
