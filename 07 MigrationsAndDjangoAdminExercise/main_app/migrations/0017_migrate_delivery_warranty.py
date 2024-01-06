# Generated by Django 4.2.6 on 2023-10-28 14:06


from django.db import migrations
from django.utils import timezone


def update_delivery_warranty(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')

    for order in order_model.objects.all():
        if order.status == "Pending":
            order.delivery = order.order_date + timezone.timedelta(days=3)
            order.save()
        elif order.status == "Completed":
            order.warranty = "24 months"
            order.save()
        elif order.status == "Canceled":
            order.delete()


def reverse_delivery_and_warranty(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')

    for order in order_model.objects.all():
        if order.status == "Pending":
            order.delivery = None
        elif order.status == "Completed":
            order.warranty = "No warranty"

        order.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_order'),
    ]

    operations = [
        migrations.RunPython(update_delivery_warranty, reverse_code=reverse_delivery_and_warranty)
    ]
