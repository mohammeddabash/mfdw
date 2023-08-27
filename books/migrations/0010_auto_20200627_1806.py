# Generated by Django 3.0.7 on 2020-06-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20200627_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, choices=[('book', 'book'), ('record', 'records'), ('lecture', 'lecture')], default='book', max_length=40),
        ),
    ]
