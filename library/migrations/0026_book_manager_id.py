# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-16 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0025_reader_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='manager_id',
            field=models.CharField(default='无', max_length=20),
        ),
    ]
