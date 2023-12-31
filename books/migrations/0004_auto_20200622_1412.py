# Generated by Django 3.0.7 on 2020-06-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_book_download_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pub_date',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='book_describtion',
            field=models.TextField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_download_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
