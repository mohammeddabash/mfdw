# Generated by Django 3.0.7 on 2020-06-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20200627_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, choices=[('book', 'book'), ('record', 'records'), ('lecture', 'lecture')], max_length=40),
        ),
    ]
