# Generated by Django 3.0.8 on 2020-08-19 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200819_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='category',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
