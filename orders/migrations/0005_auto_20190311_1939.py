# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-11 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190311_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expiry_date',
            field=models.DateField(help_text=b'MM/YYYY'),
        ),
    ]
