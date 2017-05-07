# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plugin',
            name='date',
        ),
        migrations.RemoveField(
            model_name='plugin',
            name='file',
        ),
        migrations.RemoveField(
            model_name='plugin',
            name='version',
        ),
    ]
