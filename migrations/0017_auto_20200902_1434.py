# Generated by Django 3.0.8 on 2020-09-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20200827_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='image',
            field=models.URLField(blank=True, max_length=100000),
        ),
    ]
