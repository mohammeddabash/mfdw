# Generated by Django 3.0.7 on 2020-06-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20200627_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_photo',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
    ]
