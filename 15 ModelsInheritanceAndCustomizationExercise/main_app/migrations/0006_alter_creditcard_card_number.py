# Generated by Django 4.2.7 on 2023-11-11 11:22

from django.db import migrations
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_creditcard_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='card_number',
            field=main_app.models.MaskedCreditCardField(verbose_name='verbose_name'),
        ),
    ]