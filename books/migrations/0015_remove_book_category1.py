# Generated by Django 3.0.7 on 2020-07-01 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_book_category1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category1',
        ),
    ]
