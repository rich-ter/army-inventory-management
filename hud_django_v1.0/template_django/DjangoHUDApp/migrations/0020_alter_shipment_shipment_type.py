# Generated by Django 5.0.6 on 2024-06-05 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoHUDApp', '0019_productcategory_productusage_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='shipment_type',
            field=models.CharField(choices=[('IN', 'Εισερχόμενη'), ('OUT', 'Εξερχόμενη')], max_length=3),
        ),
    ]
