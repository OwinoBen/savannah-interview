# Generated by Django 4.2.5 on 2023-09-14 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='user',
            new_name='customer',
        ),
    ]
