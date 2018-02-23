# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-21 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='item_set',
        ),
        migrations.AddField(
            model_name='reserve',
            name='time',
            field=models.ForeignKey(default='000000', on_delete=django.db.models.deletion.CASCADE, to='hospital.Time'),
            preserve_default=False,
        ),
    ]
