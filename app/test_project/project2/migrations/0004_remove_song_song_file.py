# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-18 18:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project2', '0003_auto_20180218_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='song_file',
        ),
    ]
