# Generated by Django 4.2.6 on 2023-10-28 08:07

from django.db import migrations


def create_unique_brands(apps, schema_editor):
    shoe = apps.get_model('main_app', 'Shoe')
    unique_brands = apps.get_model('main_app', 'UniqueBrands')

    unique_brand_names = shoe.objects.values_list('brand', flat=True).distinct()

    for brand_name in unique_brand_names:
        unique_brands.create(brand_name=brand_name)


def delete_unique_brands(apps, schema_editor):
    unique_brands = apps.get_model('main_app', 'UniqueBrands')

    unique_brands.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands, reverse_code=delete_unique_brands)
    ]
