# Generated by Django 3.0.3 on 2020-02-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0010_remove_autor_author_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='author_picture',
            field=models.ImageField(default=None, upload_to='C:/Users/Марина/Desktop/practice'),
        ),
    ]