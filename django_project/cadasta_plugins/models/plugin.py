from __future__ import unicode_literals

from django.db import models
from tag import Tag


class Plugin(models.Model):

    name = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )

    homepage = models.URLField(
        max_length=200,
        null=True,
        blank=True
    )

    tracker = models.URLField(
        max_length=200,
        null=True,
        blank=True
    )

    create_date = models.DateField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    about = models.TextField(
        null=True,
        blank=True
    )

    tags = models.ManyToManyField(Tag)

    # noinspection PyClassicStyleClass
    class Meta:
        app_label = 'cadasta_plugins'
        ordering = ['name']

    def __str__(self):
        return '%s' % (self.name)
