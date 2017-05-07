# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadasta_plugins', '0002_auto_20170502_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=20, null=True, blank=True)),
                ('date', models.DateField()),
                ('file', models.FileField(upload_to='plugins/')),
                ('plugin', models.ForeignKey(to='cadasta_plugins.Plugin')),
            ],
        ),
    ]
