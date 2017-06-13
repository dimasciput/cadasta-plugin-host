from __future__ import unicode_literals

import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models

from plugins.models.plugin import Plugin


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name):
        """Returns a filename that's free on the target storage system, and
        available for new content to be written to.

        Found at http://djangosnippets.org/snippets/976/

        This file storage solves overwrite on upload problem. Another
        proposed solution was to override the save method on the model
        like so (from https://code.djangoproject.com/ticket/11663):

        def save(self, *args, **kwargs):
            try:
                this = MyModelName.objects.get(id=self.id)
                if this.MyImageFieldName != self.MyImageFieldName:
                    this.MyImageFieldName.delete()
            except: pass
            super(MyModelName, self).save(*args, **kwargs)
        """
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class Release(models.Model):

    version = models.CharField(
            max_length=20,
            null=False,
            blank=False)

    date = models.DateField(
            null=False,
            blank=False)

    file = models.FileField(
            upload_to='plugins/',
            storage=OverwriteStorage())

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
