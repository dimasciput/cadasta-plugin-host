from __future__ import unicode_literals

import os
from django.db import models

from cadasta_plugins.models.plugin import Plugin


class Release(models.Model):

    version = models.CharField(
            max_length=20,
            null=False,
            blank=False)

    date = models.DateField(
            null=False,
            blank=False)

    file = models.FileField(
            upload_to='plugins/')

    experimental = models.BooleanField(
            default=False
    )

    deprecated = models.BooleanField(
            default=False
    )

    repository = models.URLField(
            null=True,
            blank=True
    )

    qgis_minimum_version = models.CharField(
            max_length=10,
            null=False,
            blank=False
    )

    qgis_maximum_version = models.CharField(
            max_length=10,
            null=False,
            blank=False
    )

    plugin = models.ForeignKey(Plugin)

    def filename(self):
        return os.path.basename(self.file.name)
