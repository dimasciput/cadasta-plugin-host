# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0005_auto_20170503_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='plugin',
            name='tracker',
            field=models.URLField(blank=True, null=True),
        ),
    ]
