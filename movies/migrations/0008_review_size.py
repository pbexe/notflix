# Generated by Django 2.2 on 2019-05-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movie_vectors'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='size',
            field=models.FloatField(default=0.0),
        ),
    ]
