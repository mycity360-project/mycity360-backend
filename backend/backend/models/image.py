# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
import os

from django.db import models
from django.utils.timezone import now as timezone_now

from ..utils.core import Core
from ..managers.image import ImageManager, ImageQueryset
from ..constants import MEDIA_ROOT, SERVER_BASE_URL


def upload_to(instance, filename):
    now = timezone_now()
    base, ext = os.path.splitext(filename)
    ext = ext.lower()
    return f"{MEDIA_ROOT}/{now:%Y/%m/%Y%m%d%H%M%S}{ext}"


class Image(Core):
    """
    Description of Image Model
    """

    image = models.URLField(_("Image URL"), null=True, blank=True)
    image_new = models.ImageField(
        _("Image"), null=True, blank=True, upload_to="image/"
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


@receiver(pre_save, sender=Image)
def create_profile(sender, instance, **kwargs):
    instance.image = f"{SERVER_BASE_URL}image/{instance.image_new.name}"
