# Generated by Django 3.0.7 on 2020-06-22 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='models',
            new_name='book',
        ),
    ]
