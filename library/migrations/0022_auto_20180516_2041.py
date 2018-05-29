# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-16 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0021_auto_20170219_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField()),
                ('date_due_to_returned', models.DateField()),
                ('date_returned', models.DateField(null=True)),
                ('amount_of_fine', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': '预约',
                'verbose_name_plural': '预约',
            },
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
        migrations.AlterModelOptions(
            name='borrowing',
            options={'verbose_name': '借阅', 'verbose_name_plural': '借阅'},
        ),
        migrations.AlterModelOptions(
            name='reader',
            options={'verbose_name': '读者', 'verbose_name_plural': '读者'},
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='reader',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='reader',
            name='status',
            field=models.IntegerField(choices=[(0, 'normal'), (-1, 'overdue')], default=0),
        ),
        migrations.AddField(
            model_name='ordering',
            name='ISBN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book'),
        ),
        migrations.AddField(
            model_name='ordering',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Reader'),
        ),
    ]
