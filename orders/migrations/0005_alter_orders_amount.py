# Generated by Django 4.2.5 on 2023-09-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orderitems_options_alter_orders_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.FloatField(default=0.0, verbose_name='Order Amount'),
        ),
    ]
