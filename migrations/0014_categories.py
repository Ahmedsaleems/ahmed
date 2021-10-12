# Generated by Django 3.0.8 on 2020-08-22 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20200823_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=64)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryitems', to='auctions.auctionlisting')),
            ],
        ),
    ]
