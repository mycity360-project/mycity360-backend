# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..utils.core import Core
from ..managers.image import ImageManager, ImageQueryset
from ..utils.services import get_file_path

from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class Image(Core):
    """
    Description of Image Model
    """

    image = models.ImageField(
        _("Image"), upload_to=get_file_path, storage=gd_storage, max_length=1024
    )

    objects = ImageManager.from_queryset(ImageQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)
