# Generated by Django 4.2.5 on 2023-09-14 22:03

from django.db import migrations, models
import util.helper


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=util.helper.image_path),
        ),
    ]
