# Generated by Django 3.1 on 2020-08-10 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0026_auto_20200810_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='listing_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
