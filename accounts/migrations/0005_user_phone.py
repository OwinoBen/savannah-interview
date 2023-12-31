# Generated by Django 4.2.5 on 2023-09-15 11:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_fist_name_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')], verbose_name='Phone number'),
        ),
    ]
