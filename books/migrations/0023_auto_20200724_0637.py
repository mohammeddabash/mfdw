# Generated by Django 3.0.7 on 2020-07-24 04:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0022_auto_20200724_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 24, 4, 37, 45, 233916, tzinfo=utc), null=True),
        ),
    ]
