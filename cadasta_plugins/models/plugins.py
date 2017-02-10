from __future__ import unicode_literals

from django.db import models


class Plugin(models.Model):

    name = models.CharField(
            max_length=200,
            null=True,
            blank=True)

    version = models.CharField(
            max_length=20,
            null=True,
            blank=True)

    date = models.DateField(
            null=False,
            blank=False)

    file = models.FileField(
            upload_to='plugins/')
