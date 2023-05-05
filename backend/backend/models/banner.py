# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from gdstorage.storage import GoogleDriveStorage
from ..utils.core import Core
from ..managers.banner import BannerManager, BannerQueryset
from ..models.area import Area

from ..utils.services import get_file_path

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class Banner(Core):
    """
    Description of Banner Model
    """

    redirect_url = models.URLField(
        _("Redirect URL"),
    )

    area = models.ForeignKey(
        verbose_name=_("Area"),
        to=Area,
        related_name="banner_area",
        on_delete=models.CASCADE,
    )
    image = models.URLField(
        _("Image"),
        null=True,
        blank=True
    )
    url = models.URLField(
        _("Image"),
        null=True,
        blank=True
    )

    objects = BannerManager.from_queryset(BannerQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")

    def __str__(self):
        return self.redirect_url

    def __unicode__(self):
        return self.redirect_url
