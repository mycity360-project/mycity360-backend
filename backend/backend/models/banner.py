# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
import os
from uuid import uuid4

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..utils.core import Core
from ..managers.banner import BannerManager, BannerQueryset
from ..models.area import Area
from ..constants import SERVER_BASE_URL


def upload_to(instance, filename):
    base, ext = os.path.splitext(filename)
    ext = ext.lower()
    return f"banner/{uuid4()}{ext}"


class Banner(Core):
    """
    Description of Banner Model
    """

    redirect_url = models.URLField(
        _("Redirect URL"),
        null=True,
        blank=True
    )

    area = models.ForeignKey(
        verbose_name=_("Area"),
        to=Area,
        related_name="banner_area",
        on_delete=models.CASCADE,
    )
    image = models.URLField(_("Image URL"), null=True, blank=True)
    image_data = models.ImageField(
        _("Image"), null=True, blank=True, upload_to=upload_to
    )
    sequence = models.PositiveIntegerField(_("Sequence"), default=0)
    objects = BannerManager.from_queryset(BannerQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)


@receiver(post_save, sender=Banner)
def create_profile(sender, instance, **kwargs):
    if instance.image != f"{SERVER_BASE_URL}{instance.image_data}":
        instance.image = f"{SERVER_BASE_URL}{instance.image_data}"
        instance.save()
