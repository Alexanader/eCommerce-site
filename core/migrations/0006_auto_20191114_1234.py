# Generated by Django 2.2 on 2019-11-14 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
