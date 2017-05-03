from __future__ import unicode_literals

from django.db import models

from cadasta_plugins.models.plugin import Plugin


class Release(models.Model):

    version = models.CharField(
            max_length=20,
            null=True,
            blank=True)

    date = models.DateField(
            null=False,
            blank=False)

    file = models.FileField(
            upload_to='plugins/')

    plugin = models.ForeignKey(Plugin)
