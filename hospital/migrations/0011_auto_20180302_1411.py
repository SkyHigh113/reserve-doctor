# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-02 05:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_auto_20180302_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='gungu',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='sido',
        ),
    ]
