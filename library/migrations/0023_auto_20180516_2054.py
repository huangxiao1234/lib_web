# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-16 12:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0022_auto_20180516_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordering',
            name='date_due_to_returned',
        ),
        migrations.RemoveField(
            model_name='ordering',
            name='date_issued',
        ),
        migrations.RemoveField(
            model_name='ordering',
            name='date_returned',
        ),
    ]
