# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-06 09:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_sildepic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='account',
        ),
    ]
