# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='number_phone',
            field=models.CharField(max_length=16),
        ),
    ]
