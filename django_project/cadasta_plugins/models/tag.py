from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):

    name = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )

    def __str__(self):
        return '%s' % self.name
