# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-02 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_auto_20180228_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='code',
            field=models.CharField(default='00', max_length=3),
            preserve_default=False,
        ),
    ]
