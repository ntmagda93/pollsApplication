# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 13:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_nowymodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NowyModel',
        ),
    ]
