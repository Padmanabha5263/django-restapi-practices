# Generated by Django 5.0.3 on 2024-03-29 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0002_alter_percustoemr_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PerCustoemr',
            new_name='PerCustomer',
        ),
        migrations.AlterModelTable(
            name='percustomer',
            table='per_customer',
        ),
    ]
