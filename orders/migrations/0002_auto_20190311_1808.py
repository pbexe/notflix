# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-11 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expiry_date',
            field=models.CharField(help_text=b'MM/YYYY', max_length=7),
        ),
    ]