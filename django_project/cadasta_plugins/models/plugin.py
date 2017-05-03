from __future__ import unicode_literals

from django.db import models


class Plugin(models.Model):

    name = models.CharField(
            max_length=200,
            null=True,
            blank=True)

    # noinspection PyClassicStyleClass
    class Meta:
        app_label = 'cadasta_plugins'
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name)
