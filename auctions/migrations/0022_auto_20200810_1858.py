# Generated by Django 3.1 on 2020-08-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_comments_listing_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='listing_category',
            field=models.CharField(max_length=20),
        ),
    ]