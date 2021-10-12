# Generated by Django 3.0.8 on 2020-08-21 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200821_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingcreator',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listingid', to='auctions.auctionlisting'),
        ),
        migrations.AlterField(
            model_name='listingcreator',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
