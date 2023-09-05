# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
import os
from uuid import uuid4

from django.db import models
from django.utils.timezone import now as timezone_now
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from ..utils.google_api import delete_image as delete_local_image


from ..utils.core import Core
from ..managers.image import ImageManager, ImageQueryset
from ..constants import MEDIA_ROOT, SERVER_BASE_URL


def upload_to(instance, filename):
    base, ext = os.path.splitext(filename)
    ext = ext.lower()
    return f"image/{uuid4()}{ext}"


class Image(Core):
    """
    Description of Image Model
    """

    image = models.URLField(_("Image URL"), null=True, blank=True)
    image_new = models.ImageField(
        _("Image"), null=True, blank=True, upload_to=upload_to
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


@receiver(post_save, sender=Image)
def create_profile(sender, instance, **kwargs):
    if (
        instance.image_new
        and instance.image != f"{SERVER_BASE_URL}{instance.image_new}"
    ):
        instance.image = f"{SERVER_BASE_URL}{instance.image_new}"
        instance.save()


@receiver(pre_delete, sender=Image)
def create_profile(sender, instance, **kwargs):
    delete_local_image(instance.image)
