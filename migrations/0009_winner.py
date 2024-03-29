# Generated by Django 3.0.8 on 2020-08-21 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listingcreator'),
    ]

    operations = [
        migrations.CreateModel(
            name='winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winningitem', to='auctions.auctionlisting')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winninguser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
