# Generated by Django 3.0.3 on 2020-02-23 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0011_autor_author_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='author_picture',
            field=models.ImageField(default=None, upload_to='bookapp/static/bookapp'),
        ),
    ]