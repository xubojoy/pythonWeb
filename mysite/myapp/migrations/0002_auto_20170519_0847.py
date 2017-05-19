# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default='xubojoy', max_length=60),
        ),
        migrations.AddField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(choices=[('s', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='M', max_length=1),
        ),
    ]
