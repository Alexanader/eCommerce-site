# Generated by Django 2.2 on 2019-11-18 14:50

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_billingaddress_payment_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='countries',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
