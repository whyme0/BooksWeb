# Generated by Django 3.0.3 on 2020-02-23 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0013_auto_20200223_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_picture',
            field=models.ImageField(default=None, upload_to='bookapp/static/bookapp/pictures'),
        ),
    ]